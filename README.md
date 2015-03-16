## Catalan HyperText Markup Language
An attempt to make HTML easier to write in simple text editors using brackets.
The name comes from the [Catalan numbers](https://en.wikipedia.org/wiki/Catalan_number),
as the design is based around brackets.

### Basic idea
Instead of 
```html
<div>
    <p class="silly">Hello, World!</p>
</div>
```
users should only have to type something like
```html
(div
  (p class: silly; 'Hello, World!')
)
```
Or, for the power user, something like `(div [p class:silly; 'Hello, World!'])`
(i.e. using interchangeable `(.)`s and `[.]`s.
### Implementation
The program will be a Python script that will output `.html` files, just like Markdown.
The inverse should be possible to: any `.html` should be easily translated to 
`.chtml` (or perhaps `.cht` for short) for working.

### Possible (plausible?) features
- flag to dot `.cht` files when compiling `.html` files
