<p align="center">
    <img alt="Cattle Logo" src="/assets/img/logo.png" height="200" />
    <h3 align="center">Cattle</h3>
    <p align="center">A Platform to Run and Share Code.</p>
    <p align="center">
        <a href="https://github.com/Clivern/Cattle/actions/workflows/ci.yml">
            <img src="https://github.com/Clivern/Cattle/actions/workflows/ci.yml/badge.svg"/>
        </a>
    </p>
</p>

Cattle is a `django` based web application. It uses `mysql` as a datastore, `redis` for Async workload and `docker` with [gvisor](https://github.com/google/gvisor) to spin isolated environments to run the code.


## Deployment

You can either deploy it manually like glamorous old days or [use terraform & ansible to deploy cattle on digitalocean or other cloud providers](https://github.com/Clivern/Cattle/tree/main/deployment/ubuntu).


## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Cattle is maintained under the [Semantic Versioning guidelines](https://semver.org/) and release process is predictable and business-friendly.

See the [Releases section of our GitHub project](https://github.com/clivern/cattle/releases) for changelogs for each release version of Cattle. It contains summaries of the most noteworthy changes made in each release. Also see the [Milestones section](https://github.com/clivern/cattle/milestones) for the future roadmap.


## Bug tracker

If you have any suggestions, bug reports, or annoyances please report them to our issue tracker at https://github.com/clivern/cattle/issues


## Security Issues

If you discover a security vulnerability within Cattle, please send an email to [hello@clivern.com](mailto:hello@clivern.com)


## Contributing

We are an open source, community-driven project so please feel free to join us. see the [contributing guidelines](CONTRIBUTING.md) for more details.


## Credits

Shoutout to these open source projects and their maintainers.

- [Django.](https://www.djangoproject.com/)
- [Django-RQ](https://github.com/rq/django-rq)
- [Requests](https://github.com/psf/requests)
- [VueJs](https://github.com/vuejs/vue)
- [Pindo](https://github.com/Clivern/Pindo)
- [and other projects ...](requirements.txt)


## License

© 2021, Cattle. Released under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

**Cattle** is authored and maintained by [@Clivern](https://github.com/clivern).
