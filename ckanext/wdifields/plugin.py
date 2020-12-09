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
                'title': [NOT_EMPTY, CONVERT_TO_EXTRAS, UNICODE],
                'update_interval_months': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'known_uses_of_data': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_collection_procedures': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_quality_procedures': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_owner_organization': [NOT_EMPTY, CONVERT_TO_EXTRAS, UNICODE],
                'data_owner_contact_name': [NOT_EMPTY, CONVERT_TO_EXTRAS, UNICODE],
                'data_owner_contact_email': [EMAIL_VALIDATOR, CONVERT_TO_EXTRAS, UNICODE],
                'data_collection_organization': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_collection_contact_name': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_collection_contact_email': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE, EMAIL_VALIDATOR],
                'data_qaqc_organization': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_qaqc_contact_name': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'data_qaqc_contact_email': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE, EMAIL_VALIDATOR],
                'funding_agency_organization': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'funding_agency_contact_name': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE],
                'funding_agency_contact_email': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE, EMAIL_VALIDATOR],
                'coordinate_system': [IGNORE_MISSING, CONVERT_TO_EXTRAS, UNICODE]
            })
        return schema

    def show_package_schema(self):
        schema = super(WdifieldsPlugin, self).show_package_schema()

        schema.update({
            'known_uses_of_data': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_collection_procedures': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_quality_procedures': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_owner_organization': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_owner_contact_name': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_owner_contact_email': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_collection_organization': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_collection_contact_name': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_collection_contact_email': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_qaqc_organization': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_qaqc_contact_name': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'data_qaqc_contact_email': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'funding_agency_organization': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'funding_agency_contact_name': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'funding_agency_contact_email': [CONVERT_FROM_EXTRAS, IGNORE_MISSING],
            'coordinate_system': [CONVERT_FROM_EXTRAS, IGNORE_MISSING]
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
