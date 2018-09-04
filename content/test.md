+++
title = "Test Post"
date = 2018-09-03
+++

Et et `exercitationem` odio *necessitatibus* omnis. Dolorem **architecto** temporibus explicabo quia vel aut. Tenetur accusantium adipisci error. Dolorum optio veritatis odio.

Necessitatibus quod minima quis qui eligendi fugit. Sint et natus quis odit perspiciatis sint. Quod neque et ut. Iusto et libero odio omnis voluptatum natus. Illum deserunt corrupti quia ducimus voluptatem et quia.

### `monospace`-Heading

Enim dignissimos aspernatur dolor aperiam iure vero qui. Sapiente a in itaque iste omnis qui. Repudiandae quaerat at qui non aut optio accusamus esse. Earum sequi modi inventore sed dolores. Enim qui rerum vel. Et veniam magni vitae animi et fuga.

> Unde quibusdam nisi qui aperiam ea omnis. Libero facilis dolor perspiciatis. Qui ipsam non fugit eum explicabo voluptas rerum. Culpa est ut nobis quas distinctio est accusamus. Ab eos similique optio.
> Autem adipisci officia sunt reprehenderit nihil. Occaecati minus veritatis quos consequatur voluptatibus enim aut. Molestias quasi ex deleniti. Odio et ipsum at distinctio autem numquam. Harum ipsam laboriosam blanditiis sit.

{{ tile_note() }}

A *note* with `monospace` **styling**.
{{ tile_end() }}

---

# Code

```rust
#[derive(Debug, Clone)]
struct Foo {
    bar: String,
    baz: i32,
}

fn main() {
    let x = Foo {
        bar: "Hello World!".to_string(),
        baz: 42,
    };

    println!("{:?}", x);
}
```

---

```python
def main():
    pass
```

---

# Lists

## Unordered List

* More
* and
* more
* Bullets

## Ordered List

1. Ordered
2. List
3. With
4. Many
5. Steps

---

{{ tile_warning() }}

**Warning:** Lorem ipsum dolor sit amet
{{ tile_end() }}

{{ tile_danger() }}

**Warning:** Lorem ipsum dolor sit amet
{{ tile_end() }}

# Table

| Foo | Bar |
| --- | --- |
| Hello | World |
| Bar | Baz |

---

# Image

![rahix](../img/rahix.svg)

---

# Long Table

| Feature     | Mutex                                                                                               | Manager                         |
|-------------|-----------------------------------------------------------------------------------------------------|---------------------------------|
| **std**     | [`std::sync::Mutex`](https://doc.rust-lang.org/nightly/std/sync/struct.Mutex.html)                  | `shared_bus::StdBusManager`     |
| **cortexm** | [`cortex_m::interrupt::Mutex`](https://docs.rs/cortex-m/0.5.6/cortex_m/interrupt/struct.Mutex.html) | `shared_bus::CortexMBusManager` |
