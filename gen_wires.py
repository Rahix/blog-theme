import json

def style(width: float) -> None:
    print(f'<defs>')
    print(f'    <style>')
    print(f'        g.wire-group .wire {{')
    print(f'            stroke-width: {width}px;')
    print(f'        }}')
    print(f'    </style>')
    print(f'</defs>')

def main() -> None:
    with open("wires.json") as f:
        data = json.load(f)

    width = data["width"]
    radius = data["radius"]

    print("{% macro js() %}")
    style(width)
    for w in data["data"]:
        first = w["path_a"][0]
        points_anim = " L ".join(f"{x} {y}" for x, y in w["path_a"])
        points_static = " L ".join(f"{x} {y}" for x, y in w["path_b"])
        print(f'<g class="wire-group wire-color-{w["color"]}">')
        print(f'    <path class="wire anim" d="M {points_anim}" />')
        print(f'    <path class="wire" d="M {points_static}" />')
        print(f'    <circle cx="{first[0]}" cy="{first[1]}" r="{radius}" class="wire" />')
        print(f'</g>')
    print("{% endmacro js %}")
    print("")
    print("{% macro nojs() %}")
    style(width)
    for w in data["data"]:
        first = w["path_b"][0]
        points_static = " L ".join(f"{x} {y}" for x, y in w["path_b"])
        print(f'<g class="wire-group wire-color-{w["color"]}">')
        print(f'    <path class="wire" d="M {points_static}" />')
        print(f'    <circle cx="{first[0]}" cy="{first[1]}" r="{radius}" class="wire" />')
        print(f'</g>')
    print("{% endmacro nojs %}")


if __name__ == "__main__":
    main()
