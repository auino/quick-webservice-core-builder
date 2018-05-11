# quick-webservice-base-builder
Quickly build the core components of a web service based system

### Introduction ###

This program allows you to quickly build the base components a [proof-of-concept](https://en.wikipedia.org/wiki/Proof_of_concept) product based on web services.

Essentially, you define the core components of the system and how they interact. Hence, the program will build an early version of the entire system in just a few seconds, by automatically implementing the defined components and by automatically coding all the interactions of the system.

### Features ###

 * Quicker PoC implementation
 * REST API support
 * Easily extensible
 * Platform independent
 * Logging capabilities
 * SSL support

### Usage instructions ###

Let's suppose you want to create a simple system composed of three components `A`, `B` and `C` and by interacting as follows (see a sample [architecture](https://www.websequencediagrams.com/?lz=dGl0bGUgU2FtcGxlIHByb2dyYW0KCkEtPkI6IGEyYgpCLT5DOiBiMmMKQy0-QTogYzJh&s=default)):
 * `A` interacts with `B`, through the `a2b` REST API method provided by `B`
 * `B` interacts with `C`, through the `b2c` REST API method provided by `C`
 * `C` interacts with `A`, through the `c2a` REST API method provided by `A`

In this case, it is required to formally define the structure of the system, through a dedicated JSON file (see the [sample.json](https://github.com/auino/quick-webservice-base-builder/blob/master/sample.json) file).
Such file includes all the core information of the system.

In addition, a component to automatically log all components interactions may be enabled.

#### Installation ####

Just clone the repository:

```
git clone https://github.com/auino/quick-webservice-base-builder.git
```

#### Configuration ####

Just copy and edit the [sample.json](https://github.com/auino/quick-webservice-base-builder/blob/master/sample.json) file provided as needed.

#### Execution ####

Just run a shell command like the following one:

```
python builder.py sample.json /tmp/out/
```

where `sample.json` identifies the JSON file including all system information and `/tmp/out/` is the main output directory.

### Builders ###

The program supports the adoption of builders for different programming languages.

#### Python ####

The Python builder allows you to create modules core code for the [Python](https://www.python.org) programming language.

##### Notes ######

 * If SSL is enabled for some modules, remember to put SSL certificate files (`certificate.crt` and `certificate.key`) on the `ssl` sub-directory of each module.
 * Outgoing methods are implemented by never called from the programs. Therefore, you have to implement your logic on the generated programs in order to make them appear.
 * The `DEBUG` variable (default to `True`) overrides sent/received data with sample data specified in the input JSON file. In order to avoid the override, set the variable to `False`.

### Contribute ###

Essentially, any support is welcome.
You can contribute to the project in two ways:
 * By enhancing the current version of the program
 * By implementing additional builders for additional programming languages

### Contacts ###

You can find me on Twitter as [@auino](https://twitter.com/auino).
