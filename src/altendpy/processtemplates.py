import importlib.util
import pathlib

import attr
import jinja2

import altendpy.compat


class SuffixNotFoundError(Exception):
    pass


def result_path(
        source,
        template_suffix,
):
    suffix = source.suffix
    if not suffix.endswith(template_suffix):
        message = 'Suffix {template_suffix!r} not found: {source!r}'.format(
            template_suffix=template_suffix,
            source=altendky.compat.fspath(source),
        )
        raise SuffixNotFoundError(message)

    return source.with_suffix(suffix[:-len(template_suffix)])


def render(source, destination, context={}, encoding='utf-8', newline='\n'):
    environment = jinja2.Environment(
        undefined=jinja2.StrictUndefined,
        loader=jinja2.FileSystemLoader(altendpy.compat.fspath(source.parent)),
        newline_sequence=newline,
        autoescape=False,
        trim_blocks=True,
    )
    template = environment.get_template(name=source.name)

    rendered = template.render(context)
    rendered = rendered.rstrip() + newline

    encoded = rendered.encode(encoding)

    if destination.read_bytes() != encoded:
        destination.write_bytes(encoded)


@attr.s
class RelativeImporter:
    root = attr.ib()

    def __call__(self, location):
        location = pathlib.Path(location)

        full_path = self.root / location
        module_name = location.stem

        spec = importlib.util.spec_from_file_location(
            name=module_name,
            location=full_path,
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module


def process_root(root, suffix, output=None):
    paths = root.rglob('*.*{suffix}'.format(suffix=suffix))

    for path in paths:
        if output is not None:
            message = 'Handling: {path!r}'.format(
                path=altendpy.compat.fspath(path),
            )
            output(message)

        render(
            source=path,
            destination=result_path(path, template_suffix=suffix),
            context={
                'importer': RelativeImporter(root=path.parent),
            },
        )
