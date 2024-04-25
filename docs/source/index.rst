
sphinxcontrib-data-pipeline
===========================

This extension allows you to document data processing pipelines that connect
tools ("drivers") and corresponding data products in sphinx.

* `Repository <https://github.com/michaelbuehlmann/sphinxcontrib-data-pipeline>`_
* `Documentation <https://michaelbuehlmann.github.io/sphinxcontrib-data-pipeline>`_

Installation
------------

You can install the extension via pip:

.. code-block:: bash

   pip install sphinxcontrib-data-pipeline

Getting Started
---------------

To use this extension, add the following extensions to the `extensions` list
in your `conf.py` file:

.. code-block:: python

   extensions = [
      ...
      "sphinxcontrib_data_pipeline",
      "sphinxcontrib.mermaid",
      "sphinx_tabs.tabs",
      "sphinx_toolbox.collapse"
   ]

Data Products
^^^^^^^^^^^^^

A data product can be added with the `data_product` directive.
The directive has the following options:

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

A driver can be added with the `driver` directive.
The directive has the following options:

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

For `:inputs:` and `:outputs:` you can specify a list of data products that are
expected as input or produced as output. Make sure to use the same name as in the
data product directive.

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

A pipeline is specified by a set of drivers and data products that are
linked together. The following example specifies 4 data products and 2 drivers.

.. code-block:: text

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


The entire pipeline can be shown in a single diagram by using the `pipeline` directive:

.. code-block:: text

   .. pipeline::


.. pipeline::


Externally Specifying Data Products and Drivers
-----------------------------------------------

You can specify Data Products and Drivers in a separate file. You will need to
provide a parser for your file type and register it in the Sphinx ``conf.py`` file
as:

.. code-block:: python

   # workflows parsers
   driver_parser = "package.module:parse_driver_function"
   data_product_parser = "package.module:parse_dataproducts_function"


See the `example_yaml_parser.py <https://github.com/michaelbuehlmann/sphinxcontrib-data-pipeline/blob/master/sphinxcontrib_data_pipeline/parsers/example_yaml_parser.py>`
file for an example of how to implement a parser for a yaml file.

You can then use the ``.. external_data_products::`` and ``.. external_drivers::`` directives to include the data products and drivers from the external file.
For example:

.. code-block:: text

   .. external_data_products:: path/to/specification_file.yaml
      :type: path

   .. external_drivers:: path/to/specification_file.yaml
      :type: path

The files can also be hosted in an external repository:

.. code-block:: text

   .. external_data_products:: path/in/repository.yaml
    :type: git
    :git-branch: master
    :git-url: https://url_to_git_repo.com/repository.git

Example
^^^^^^^

The following example shows how to use the external data products and drivers directives. We specify a pipeline in
`example_specs.yaml <https://github.com/michaelbuehlmann/sphinxcontrib-data-pipeline/blob/master/sphinxcontrib_data_pipeline/docs/source/example_specs.yaml>`_.
and include it here with the following code:

.. code-block:: text

   .. external_data_products:: example_specs.yaml
      :type: path

   .. external_drivers:: example_specs.yaml
      :type: path

.. external_data_products:: ./example_specs.yaml
   :type: path

.. external_drivers:: ./example_specs.yaml
   :type: path
