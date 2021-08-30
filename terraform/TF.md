# Best practices to create & organize Terraform code
1. Use separate state locations based on logical environment boundaries.
2. Keep your modules and your environment implementation code separate.
3. Decompose and abstract your terraform code to maximize reuse.
4. Encryption of credentials is important!
5. Use variable files:

    They can be set in a number of ways:
    * In variable.tf file
    * Individually, with the -var command-line option.
    * In variable definitions (.tfvars) files, either specified on the command line or automatically loaded.
    * As environment variables.
5. Structuring of Terraform configurations:

    Terraform code can be written in a single file but it would be better if we have several files split logically:
    * main.tf — call modules, locals and data-sources to create all the resources
    * variables.tf — contains information of variables used in main.tf
    * outputs.tf — contains outputs from the resources generated in main.tf

    By splitting the files in this format it helps in reusability and sharing of code as well as helps in improving whenever required.

## References
* https://www.xtivia.com/blog/cloud/terraform-best-practices/
* https://medium.com/xebia-engineering/best-practices-to-create-organize-terraform-code-for-aws-2f4162525a1a