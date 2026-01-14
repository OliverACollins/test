# Grid-Illusions
**A flexible Python package enabling users to draw the Hermann, scintillating, and Bergen grid illusions.**

## Rationale
The purpose of creating this Python package was to provide an easy-to-use tool for developing simple grid illusions, tractable for implementation within psychological paradigms. This is the first package that I am aware of to feature all three grid illusions.

## Illusions included in this package
### Hermann grid illusion
First described in 1870<sup>1</sup>, the Hermann grid illusion is prototypically created when looking at a white grid on top of a black background. The optical illusion experienced consists of deceptively seeing relatively faint dark patches appearing at the intersections of the grid lines.

<figure>
 <img src = "src/media/hermann.png" alt = "Default Hermann grid illusion"/>
</figure>


## Scintillating grid illusion
Created in the 1990s<sup>2</sup>, 

<figure>
 <img src = "src/media/scintillating.png" alt = "Default scintillating grid illusion"/>
</figure>

## Bergen grid illusion
TEXT HERE

<figure>
 <img src = "src/media/bergen.png" alt = "Default Bergen grid illusion"/>
</figure>


## Installation
Install directly from this GitHub repository in Python terminal:

```python
pip install https://github.com/OliverACollins/Grid-Illusions/zipball/main
```

## Usage: CLI
To generate each illusion, you can run the following commands in the Python terminal:

```python
grid-illusions hermann
```

```python
grid-illusions scintillating
```

```python
grid-illusions bergen
```


## References
<sup>1</sup> Hermann, L. (1870). Eine Erscheinung simultanen Contrastes. Pflüger, Archiv für die Gesammte Physiologie des Menschen und der Thiere, 3(1), 13–15. https://doi.org/10.1007/BF01855743
<sup>2</sup> Schrauf M, Lingelbach B, Lingelbach E & Wist ER (1995) The Hermann grid and the scintillation effect. Perception 24: suppl, 88–89

*If any issues occur with this Python package, please open an [Issue](https://github.com/OliverACollins/Grid-Illusions/issues) so that any problems highlighted can be addressed. Thank you!*