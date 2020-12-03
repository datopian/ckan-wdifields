# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.plugins.toolkit import Invalid
def is_required(value):
    if len(value)<1:
        raise Invalid("Is required.")
    return value
class WdifieldsPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)



    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(WdifieldsPlugin, self).create_package_schema()
        schema.update({'update_interval_months': [tk.get_validator('ignore_missing'),tk.get_converter('convert_to_extras')]})
	 # our custom field
        schema.update({
            'known_uses_of_data': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_procedures': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_quality_procedures': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_owner_organization': [is_required,
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_owner_contact_name': [is_required,
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_owner_contact_email': [tk.get_validator('email_validator'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_qaqc_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_qaqc_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_qaqc_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'funding_agency_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'funding_agency_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'funding_agency_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'coordinate_system': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema




    def update_package_schema(self):
        schema = super(WdifieldsPlugin, self).update_package_schema()
        # our custom field
        schema.update({'update_interval_months':[tk.get_validator('ignore_missing'), tk.get_converter('convert_to_extras')]})
        schema.update({
            'known_uses_of_data': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_procedures': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_quality_procedures': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_owner_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_owner_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_owner_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_collection_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_qaqc_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_qaqc_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'data_qaqc_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'funding_agency_organization': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'funding_agency_contact_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'funding_agency_contact_email': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema.update({
            'coordinate_system': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        return schema





    def show_package_schema(self):
        schema = super(WdifieldsPlugin, self).show_package_schema()
        schema.update({'update_interval_months': [tk.get_converter('convert_from_extras'), tk.get_validator('ignore_missing')]})
        schema.update({
            'known_uses_of_data': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_collection_procedures': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_quality_procedures': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_owner_organization': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_owner_contact_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_owner_contact_email': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_collection_organization': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_collection_contact_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_collection_contact_email': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_qaqc_organization': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_qaqc_contact_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'data_qaqc_contact_email': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'funding_agency_organization': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'funding_agency_contact_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'funding_agency_contact_email': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema.update({
            'coordinate_system': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
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
