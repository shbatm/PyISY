## PyISY

### Python Library for the ISY Controller

This library allows for easy interaction with ISY nodes, programs, program,
climate module, and network module. This class also allows for functions to be
assigned as handlers when ISY parameters are changed. ISY parameters can be
monitored automatically as changes are reported from the device.

**NOTE:** Significant changes have been made in V2, please refer to the [CHANGELOG](CHANGELOG.md) for details. It is recommended you do not update  to the latest version without testing for any unknown breaking changes or impacts to your dependent code.

### Examples

See the [examples](examples/) folder for connection examples.

### Maintainers

* Greg Laabs ([@OverloadUT])
* Ryan Kraus ([@rmkraus]) (creator)

### Contributing

A note on contributing: contributions of any sort are more than welcome! This repo uses precommit hooks to validate all code. We use `black` to format our code, `isort` to sort our imports, `flake8` for linting and syntax checks, and `codespell` for spell check.

To use [pre-commit](https://pre-commit.com/#installation), see the installation instructions for more details.

Short version:

```shell
# From your copy of the pyisy repo folder:
pip install pre-commit
pre-commit install
```

[@OverloadUT]: https://github.com/overloadut
[@rmkraus]: https://github.com/rmkraus

### PyISY_beta Fork & PyPi Package

The PyISY_beta package is a drop in replacement & testing package for the original PyISY.  It was created to provide a package to test new modifications while waiting to be incorporated into the original scope.

For more information about the beta package: https://github.com/shbatm/PyISY/tree/PyISY_beta