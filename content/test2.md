+++
title = "Test Post 2"
date = 2018-09-04
+++

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

Et et `exercitationem` odio *necessitatibus* omnis. Dolorem **architecto** temporibus explicabo quia vel aut. Tenetur accusantium adipisci error. Dolorum optio veritatis odio.


{% note() %}
## Header
### Header
Necessitatibus quod minima quis qui eligendi fugit. Sint et natus quis odit perspiciatis sint. Quod neque et ut. Iusto et libero odio omnis voluptatum natus. Illum deserunt corrupti quia ducimus voluptatem et quia.
{% end %}

{% warning() %}
## Header
### Header
Necessitatibus quod minima quis qui eligendi fugit. Sint et natus quis odit perspiciatis sint. Quod neque et ut. Iusto et libero odio omnis voluptatum natus. Illum deserunt corrupti quia ducimus voluptatem et quia.
{% end %}

{% danger() %}
## Header
### Header
Necessitatibus quod minima quis qui eligendi fugit. Sint et natus quis odit perspiciatis sint. Quod neque et ut. Iusto et libero odio omnis voluptatum natus. Illum deserunt corrupti quia ducimus voluptatem et quia.
{% end %}
