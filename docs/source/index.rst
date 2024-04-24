
sphinxcontrib-data-pipeline
===========================

This extension allows you to document data processing pipelines that connect
tools ("drivers") and corresponding data products in sphinx.

Getting Started
---------------

To use this extension, add `sphinxcontrib_data_pipeline`  and `sphinxcontrib.mermaid` to the `extensions` list
in your `conf.py` file.

Data Products
^^^^^^^^^^^^^

.. code-block:: text

   .. data_product:: Data
      :description: Description of `Data A`.
      :format: CSV
      :file_extension: .csv

.. data_product:: Data
   :description: Description of `Data A`.
   :format: CSV
   :file_extension: .csv


Drivers
^^^^^^^

.. code-block:: text

   .. driver:: tool
      :description: Description of `tool`.
      :executable: tool
      :repository: https:<path_to_repository>.com
      :documentation: https:<path_to_documentation>.com
      :contact: Max Mustermann
      :inputs:
      :outputs:

      # Command Line Arguments
      tool [options] input_file output_file

.. driver:: tool
   :description: Description of `tool`.
   :executable: tool
   :repository: https:<path_to_repository>.com
   :documentation: https:<path_to_documentation>.com
   :contact: Max Mustermann
   :inputs:
   :outputs:

   # Command Line Arguments
   tool_A [options]


Pipeline:
---------

.. data_product:: Data_A
   :description: Description of `Data A`.
   :format: text
   :file_extension: .txt

.. data_product:: Data_B
   :description: Description of `Data B`.
   :format: text
   :file_extension: .txt

.. data_product:: Data_C
   :description: Description of `Data B`.
   :format: text
   :file_extension: .txt

.. data_product:: Data_D
   :description: Description of `Data B`.
   :format: text
   :file_extension: .txt

.. driver:: Tool_A
   :description: Description of `Tool A`.
   :inputs: Data_A
   :outputs: Data_B

   # Command Line Arguments
   Tool_A [options] input_file output_file

.. driver:: Tool_B
   :description: Description of `Tool B`.
   :inputs: Data_B
   :outputs: [Data_C, Data_D]

   # Command Line Arguments
   Tool_B [options] input_file output_file

.. pipeline::