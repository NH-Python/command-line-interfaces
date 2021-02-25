

def apply_transforms(line, transforms):
    transformed = line
    for transformer in transforms:
        transformed = transformer(transformed)
    return transformed

import sys
import click
from uppercase import to_uppercase
from add_space import add_space

@click.command()
@click.argument('transform', required=False, default='')
@click.option('--uppercase', '-u', is_flag=True, flag_value=True,  help="Make uppercase")
@click.option('--addspace', '-a', is_flag=True, flag_value=True, help="Add a space between each character")
def transformer(transform:str, uppercase:bool, addspace:bool):
    """
    Transforms lines of text read from stdin
    """
    transformers = []
    if uppercase or transform == "uppercase":
        transformers.append(to_uppercase)
    if addspace or transform == "addspace":
        transformers.append(add_space)

    if not transformers:
        click.secho("At least one transform must be specified", fg="red", file=sys.stderr)
        exit(1)

    for line in sys.stdin:
        print(apply_transforms(line, transformers), end="")


if __name__ == "__main__":
    transformer()
