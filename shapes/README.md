

#### [shapes-circle](http://tangrams.github.io/blocks/#shapes-circle) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/circle.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw circles. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/circle-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float circleDF (vec2 st)`
 + `float circle (vec2 st, float radius)`
 + `float circleBorder (vec2 st, float radius)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./shapes/test/shapes-circle.png)](http://tangrams.github.io/blocks/test.html?test=./shapes/test/shapes-circle.json)

- **circle** ( mean: 0.00202213340506 median: 0.001985 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/circle-circle.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/circle-circle.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += circle(v_texcoord.xy,.5);
```


- **circleBorder** ( mean: 0.00153645898277 median: 0.001512 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/circle-circleBorder.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/circle-circleBorder.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += circleBorder(v_texcoord.xy,.5);
```


- **circleDF** ( mean: 0.00204920697922 median: 0.00198 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/circle-circleDF.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/circle-circleDF.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += circleDF(v_texcoord.xy-.5);
```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/patterns.yaml&lines=146" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/patterns.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/nursery.yaml&lines=146" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/nursery.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/lego.yaml&lines=109-110" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/lego.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-cross](http://tangrams.github.io/blocks/#shapes-cross) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/cross.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw crosses. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/cross-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float cross (vec2 st, float size, float width)`
 + `float cross (in vec2 st, float _size)`
 + `float cross (in vec2 st, vec2 _size)`

Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml&lines=181-183" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/oblivion.yaml&lines=155-156" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/oblivion.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/matrix.yaml&lines=101-104" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/matrix.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/tron.yaml&lines=122" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/tron.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-digits](http://tangrams.github.io/blocks/#shapes-digits) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/digits.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw number digits.



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/digits-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **CHAR_DECIMAL_POINT**:  The *default value* is ```10.0```. 
 -  **CHAR_MINUS**:  The *default value* is ```11.0```. 
 -  **CHAR_BLANK**:  The *default value* is ```12.0```. 

These are the **shader blocks**:

- **global**:
 + `float SampleDigit (const in float fDigit, const in vec2 vUV)`
 + `float PrintValue (const in vec2 vStringCharCoords, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces)`
 + `float PrintValue (in vec2 fragCoord, const in vec2 vPixelCoords, const in vec2 vFontSize, const in float fValue, const in float fMaxDigits, const in float fDecimalPlaces)`

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-polygons](http://tangrams.github.io/blocks/#shapes-polygons) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/polygons.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw polygons. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/polygons-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float shapeDF (vec2 st, int N)`
 + `float shape (vec2 st, int N, float width)`
 + `float shapeBorder (vec2 st, int N, float width)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./shapes/test/shapes-polygons.png)](http://tangrams.github.io/blocks/test.html?test=./shapes/test/shapes-polygons.json)

- **shapeDF** ( mean: 0.00481603499608 median: 0.004816 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/polygons-shapeDF.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/polygons-shapeDF.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += shapeDF(v_texcoord.xy,5);
```


- **shape** ( mean: 0.00490561710037 median: 0.004906 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/polygons-shape.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/polygons-shape.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += shape(v_texcoord.xy,5,.5);
```


- **shapeBorder** ( mean: 0.00499703796488 median: 0.005011 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/polygons-shapeBorder.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/polygons-shapeBorder.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += shapeBorder(v_texcoord.xy,5,.5);
```


Examples:
<a href="https://mapzen.com/tangram/play/?scene=https://tangrams.github.io/tangram-sandbox/styles/9845C.yaml&lines=153" target="_blank">
<img src="https://tangrams.github.io/tangram-sandbox/styles/9845C.png" style="width: 100%; height: 100px; object-fit: cover;">
</a>

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-rect](http://tangrams.github.io/blocks/#shapes-rect) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/rect.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw rectangles. To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/rect-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float rectDF (in vec2 st, in vec2 size)`
 + `float rectDF (in vec2 st, in float size)`
 + `float rect (in vec2 st, in vec2 size, in float radio)`
 + `float rect (vec2 st, float size, float radio)`
 + `float rectBorder (in vec2 st, in vec2 size, in float radio)`
 + `float rectBorder (vec2 st, float size, float radio)`
 + `float rect (vec2 st, vec2 size)`
 + `float rect (vec2 st, float size)`

Here are some **benchmarks** of this block performed on a Raspberry Pi:
[![](http://tangrams.github.io/blocks/./shapes/test/shapes-rect.png)](http://tangrams.github.io/blocks/test.html?test=./shapes/test/shapes-rect.json)

- **rect_rnd** ( mean: 0.00186770642702 median: 0.001949 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/rect-rect_rnd.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/rect-rect_rnd.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += rect(v_texcoord.xy,vec2(.5),.5);
```


- **rectDF** ( mean: 0.0016341938691 median: 0.001514 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/rect-rectDF.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/rect-rectDF.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += rectDF(v_texcoord.xy,vec2(.5));
```


- **rect** ( mean: 0.00151843366093 median: 0.001504 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/rect-rect.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/rect-rect.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += rect(v_texcoord.xy,vec2(.5));
```


- **rectBorder_rnd** ( mean: 0.00151967114641 median: 0.001507 )

<a href="http://thebookofshaders.com/edit.php#http://tangrams.github.io/blocks/./shapes/test/rect-rectBorder_rnd.frag"><img src="http://tangrams.github.io/blocks/./shapes/test/rect-rectBorder_rnd.png" style="width:100px; height:100px; float: right; left: 55px;"></a>

```glsl
...
// Color:
    color.rgb += rectBorder(v_texcoord.xy,vec2(.5),.5);
```


![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-simplex](http://tangrams.github.io/blocks/#shapes-simplex) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/simplex.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

Collection of functions to draw shapes using a simplex grid. To learn more about simplex grids check [this chapter about noise from the Book of Shaders](https://thebookofshaders.com/11/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/simplex-full.yaml
```


These blocks uses a custom **shader**.
These are the **shader blocks**:

- **global**:
 + `float warp (vec3 S)`
 + `float circle (vec3 S)`
 + `float triangle (vec3 S)`
 + `vec3 star (vec3 S)`
 + `vec3 sakura (vec3 S)`
 + `float lotus (vec3 S, float petals_size, float roundness)`

![](https://mapzen.com/common/styleguide/images/divider/compass-red.png)


#### [shapes-type](http://tangrams.github.io/blocks/#shapes-type) <a href="https://github.com/tangrams/blocks/blob/gh-pages/shapes/type.yaml" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a>

This block provides to functions `fill` and `stroke`. Each one transform a SDF to a fill shape or a stroke shape (border). The stroke width can be control with the define `STROKE`. 
To learn more about how to make shapes on shaders go to From check [this chapter about shapes from the Book of Shaders](https://thebookofshaders.com/07/)



To import this block add the following url to your `import` list:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/type.yaml
```




If you want to import this block together **with their dependencies** use this other url:

```yaml
import:
    - https://tangrams.github.io/blocks/shapes/type-full.yaml
```


These blocks uses a custom **shader**.
These are the **defines**:
 -  **STROKE**:  The *default value* is ```0.15```. 

These are the **shader blocks**:

- **global**:
 + `float fill (in float size, in float x)`
 + `float stroke (in float size, in float x)`
