# juicer



Service to extract clean corpus from given website.

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Credits](#credits)
* [License](#license)
* [Wiki and FAQ's](#wiki-and-faqs)


## Installation
This project uses [**Pipenv**](https://pipenv.readthedocs.io/en/latest/) to install and manage all it's package dependencies. 
To setup it, just do the following:
```shell

# Clone repor to your local directory
$ git clone git@github.com:andreffs18/juicer.git .
Cloning into 'juicer'...
(...)

# Install all project dependencies
$ pipenv install
Using /usr/local/bin/python3.6m (3.6.5) to create virtualenv…
(...)


# Activate virtual environment
$ pipenv shell
(juicer-kMLf9zVL) $ 
```


## Usage

To run this you just need to enter the following command:

```shell
(juicer-kMLf9zVL) $ scrapy crawl website -a start_url="https://www.example.com/" -o dump.json
```

This initialize a **scrapy** spider called **"website"** which will crawl all pages from **"start_url"** and output all cleaned text into **"dump.json"** file.  

## Contributing

We appreciate your contributions to this project. To do so, please follow [these](CONTRIBUTING.md) guidelines.


## Credits

This project could not have been done without **[Scrapy](https://scrapy.org/)**, the most used scraping tool on the python ecosystem. :thumbsup:


## License

[MIT License Copyright (c)](/LICENCE.md) 2018 andreffs18


## Wiki and FAQ's

We try to keep our wiki up-to-date as best as we can, so if you have any questions, please use it! 
If you don't find anything regarding what you are looking for or if you have any suggestions, then create an issue and we will look at it as soon as possible. :+1:



Fork, clone, share! 
