"""
Function to process YAML file
"""

import yaml

class YamlPipelineExecutor:
    """
    Class to handle all processing and ELT processes
    """
    def __inti__(self, pipeline_location):
        self._pipeline_location = pipeline_location

    def _load_pipeline(self):
        """
        Read configuration from YAML file
        """
        # Read the YAML file in read mode
        with open(
            self._pipeline_location,
            'r',
            encoding='utf-8'
        ) as in_file:
            _yaml_data = yaml.safe_load(in_file)
