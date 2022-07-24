# Ark Turret Optimizer - Example

This is basically a turret optimizer, but it's inspired off of Ark: Survival Evolved turret walls. The idea behind it is that turret placements have a maximum of 100 turrets within sight of each other (approx 33.333 tiles).  Each heavy turret holds about 5,280 advanced rifle ammo, and each Tek turret about 5,000 shards.  My idea is to use PSO to optimize the placement of the turrets, against several basic examples of agents accessing a particular region beyond the wall.  Despite not being able to replicate all nuances behind ark play (such as meshing, certain obstacles, and the overall Ark environment), this example serves as a prototype/basis for turret optimization ideas. For example, does it make sense to have a solid 100 turret capped wall, or a mesh of turrets throughout a base?  This program probably won't answer that, but can hint at ideas. 

## Conda

This is written in Python and uses a Conda environment to manage dependencies.  Install and activate the conda environment as follows: 

```bash
conda env create -f .\env\ark.yaml
conda activate ark
```