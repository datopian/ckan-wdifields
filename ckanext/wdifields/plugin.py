# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk

# from ckan.plugins.toolkit import Invalid

IGNORE_MISSING = tk.get_validator('ignore_missing')
CONVERT_TO_EXTRAS = tk.get_converter('convert_to_extras')
CONVERT_FROM_EXTRAS = tk.get_converter('convert_from_extras')
EMAIL_VALIDATOR = tk.get_validator('email_validator')
NOT_EMPTY = tk.get_validator('not_empty')
UNICODE = tk.get_validator('unicode_safe')
URL_VALIDATOR = tk.get_validator('url_validator')


# def is_required(value):
#     if len(value) < 1:
#         raise Invalid("Is required.")
#     return value


class WdifieldsPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(WdifieldsPlugin, self).create_package_schema()
        return self._custom_schema_hook(schema)

    def update_package_schema(self):
        schema = super(WdifieldsPlugin, self).update_package_schema()
        return self._custom_schema_hook(schema)

    def _custom_schema_hook(self, schema):
        schema.update(
            {
                # 'title': [NOT_EMPTY, CONVERT_TO_EXTRAS, UNICODE],
                'title': [NOT_EMPTY, UNICODE],
                'notes': [NOT_EMPTY, UNICODE],
                'source_url': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'division': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'subdivision': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'contact_name': [NOT_EMPTY, CONVERT_TO_EXTRAS, UNICODE],
                'contact_email': [NOT_EMPTY, EMAIL_VALIDATOR, CONVERT_TO_EXTRAS, UNICODE],
                'contact_phone': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            })
        
        schema['resources'].update({
            # 'tag_string': [NOT_EMPTY, CONVERT_TO_EXTRAS, UNICODE],
            'resource_division' : [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'resource_subdivision' : [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'data_source' : [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'resource_contact_name': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'resource_contact_email': [IGNORE_MISSING, EMAIL_VALIDATOR, CONVERT_TO_EXTRAS, UNICODE],
            'resource_contact_phone': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'data_uses': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'collection_procedures': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'collection_timeframe': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'collection_frequency': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'preparation_method': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'publish_method': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'publish_frequency': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'quality_procedures': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'resource_version': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'license_id': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'geographic_location': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'coordinate_system': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
            'data_dictionary': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
        })
        return schema

    def show_package_schema(self):
        schema = super(WdifieldsPlugin, self).show_package_schema()

        schema.update({
            'title': [NOT_EMPTY, IGNORE_MISSING],
            'source_url': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'division': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'subdivision': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'contact_name': [CONVERT_FROM_EXTRAS, NOT_EMPTY],
            'contact_email': [CONVERT_FROM_EXTRAS, NOT_EMPTY],
            'contact_phone': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
        })

        schema['resources'].update({
            # 'tag_string': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'resource_division' : [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'resource_subdivision' : [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_source' : [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'resource_contact_name': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'resource_contact_email': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'resource_contact_phone': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_uses': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'collection_procedures': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'collection_timeframe': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'collection_frequency': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'preparation_method': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'publish_method': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'publish_frequency': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'quality_procedures': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'resource_version': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'license_id': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'geographic_location': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'coordinate_system': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_dictionary': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
        })
        
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
