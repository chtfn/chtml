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
  (p class: silly; Hello, World!)
)
```
Or, for the power user, something like `(div [p class:silly; Hello, World!])`
(i.e. using interchangeable `(.)`s and `[.]`s).
### Implementation
The program will be a Python script that will output `.html` files, just like Markdown.
The inverse should be possible to: any `.html` should be easily translated to 
`.chtml` (or perhaps `.cht` for short) for working.

#### Syntactic elements
The general form will be something like `<a href="x">link</a>` → `(a href: x; link)`. 
A possible alternate canonical form would be something like `a(href: x; link)`, so the
scope of the element is very clear. This would yield
```html
div(
   p(class: silly; Hello, World!)
)
```
- A problem with this is if there are elements that are not part of the normal namespace, the parser
will freak out.
- A problem might also be that special characters cause the compiler to end the group (as they're
called in regexes) prematurely.
- Another possible problem is that the class might be a little unclear. For instance,
`<p class="silly, fancy">text</p>` → `(p class: silly, fancy; text)` renders it a little less clear,
as there is no delimiter between the list of classes and the actual contents. Perhaps this is
mitigated by enclosing the text in quotation marks, e.g. `(p class: silly, fancy; 'text')`, or
more experimental solutions such as `(p class: silly, fancy; | text)` which is quite pleasing
to the eye, though might yield other problems with keyboards other than US qwerty.


### Possible (plausible?) features
- flag to dot `.cht` files when compiling `.html` files
