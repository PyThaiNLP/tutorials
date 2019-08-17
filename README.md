
# PyThaiNLP Tutorials

The repository contains tutorial notebooks for the official documentation website.

All thte tutorial notebook are presented as sphinx-style document at:

[https://www.thainlp.org/pythainlp/tutorials](https://www.thainlp.org/pythainlp/tutorials)

## Contributing Guideline

1. Upload notebook to `source/notebooks` in  `dev`
2. Create a pull request to `master` branch
3. After the pull request is merged, the new notbook will be generated automatically and uploaded to thainlp.org/pythainlp/tutorials


## Generate documentation

1. Add a Jupyter notebook to `source/notebooks`
2. Run `make html` to build HTML document from notebooks 
3. The generated HTML files will be in `build/html`
