

def apply_transforms(line, transforms):
    transformed = line
    for transformer in transforms:
        transformed = transformer(transformed)
    return transformed


if __name__ == "__main__":
    import sys
    import argparse
    from uppercase import to_uppercase
    from add_space import add_space

    parser = argparse.ArgumentParser(description="Process text provided via STDIN")
    parser.add_argument('transform', nargs="?", default="")
    parser.add_argument('--uppercase', '-u', action='store_true')
    parser.add_argument('--addspace', '-a', action='store_true')
    output = parser.parse_args()

    transformers = []
    if output.uppercase or output.transform == "uppercase":
        transformers.append(to_uppercase)
    if output.addspace or output.transform == "addspace":
        transformers.append(add_space)

    if not transformers:
        print("At least one transform must be specified", file=sys.stderr)
        exit(1)

    for line in sys.stdin:
        print(apply_transforms(line, transformers), end="")
