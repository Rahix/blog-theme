import sys
import json
import random

def style(pre: str, width: float) -> None:
    print(f'<defs>')
    print(f'    <style>')
    print(f'        g.wire-group.p{pre} .wire {{')
    print(f'            stroke-width: {width}px;')
    print(f'            fill: transparent;')
    print(f'        }}')
    print(f'    </style>')
    print(f'</defs>')


def prefix() -> str:
    return str(random.randint(10000, 100000))


def main() -> None:
    if len(sys.argv) != 2:
        raise Exception("usage: py gen_wires.py <wires.json>")

    with open(sys.argv[1]) as f:
        data = json.load(f)

    width = data["width"]
    radius = data["radius"]

    print("{% macro js() %}")
    pre = prefix()
    style(pre, width)
    for w in data["data"]:
        first = w["path_a"][0]
        points_anim = " L ".join(f"{x} {y}" for x, y in w["path_a"])
        points_static = " L ".join(f"{x} {y}" for x, y in w["path_b"])
        print(f'<g class="wire-group wire-color-{w["color"]} p{pre}" data-wire-duration="{w["duration"]}">')
        print(f'    <path class="wire anim" d="M {points_anim}" />')
        print(f'    <path class="wire" d="M {points_static}" />')
        print(f'    <circle cx="{first[0]}" cy="{first[1]}" r="{radius}" class="wire" />')
        print(f'</g>')
    print("{% endmacro js %}")
    print("")
    print("{% macro nojs() %}")
    pre = prefix()
    style(pre, width)
    for w in data["data"]:
        first = w["path_b"][0]
        points_static = " L ".join(f"{x} {y}" for x, y in w["path_b"])
        print(f'<g class="wire-group wire-color-{w["color"]} p{pre}">')
        print(f'    <path class="wire" d="M {points_static}" />')
        print(f'    <circle cx="{first[0]}" cy="{first[1]}" r="{radius}" class="wire" />')
        print(f'</g>')
    print("{% endmacro nojs %}")


if __name__ == "__main__":
    main()
