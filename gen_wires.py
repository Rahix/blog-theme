import json


def main() -> None:
    with open("wires.json") as f:
        data = json.load(f)

    print("{% macro js() %}")
    for w in data:
        first = w["path_a"][0]
        points_anim = " L ".join(f"{x} {y}" for x, y in w["path_a"])
        points_static = " L ".join(f"{x} {y}" for x, y in w["path_b"])
        print('<g class="wire-group">')
        print(f'    <path class="wire anim" d="M {points_anim}" />')
        print(f'    <path class="wire" d="M {points_static}" />')
        print(f'    <circle cx="{first[0]}" cy="{first[1]}" r="6" class="wire" />')
        print('</g>')
    print("{% endmacro js %}")
    print("")
    print("{% macro nojs() %}")
    for w in data:
        first = w["path_b"][0]
        points_static = " L ".join(f"{x} {y}" for x, y in w["path_b"])
        print('<g class="wire-group">')
        print(f'    <path class="wire" d="M {points_static}" />')
        print(f'    <circle cx="{first[0]}" cy="{first[1]}" r="6" class="wire" />')
        print('</g>')
    print("{% endmacro nojs %}")


if __name__ == "__main__":
    main()
