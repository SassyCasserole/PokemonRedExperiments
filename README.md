# Train RL agents to play Pokemon Red!

<a href="https://youtu.be/DcYLT37ImBY">
  <img src="/assets/poke_map.gif?raw=true">
</a>

  
## Watch the [Video on Youtube!](https://youtu.be/DcYLT37ImBY)  

<a href="https://youtu.be/DcYLT37ImBY">
  <img src="/assets/Pokemon YT5 FFFFinal.jpg?raw=true" width="256">
</a>
  
## Running the Pretrained Model Interactively 🎮  
🐍 Python 3.10 is recommended. Other versions may work but have not been tested.   
You also need to install ffmpeg and have it available in the command line.

1. Copy your legally obtained Pokemon Red ROM into the `src` directory. You can find this using google, it should be 1MB. Rename it to `PokemonRed.gb` if it is not already. The sha1 sum should be `ea9bcae617fdf159b045185467ae58b2e4a48b9a`, which you can verify by running `shasum PokemonRed.gb`.
2. Install dependencies from base directory:
```pip install -e .```
3. In some cases it may be necessary to separately install the SDL libraries.
```Run installs.sh```
4. Run the pre-trained interactive tutorial first from base directory:
```interactive_tutorial```
5. You can also execute this script directly from the `src/baselines` directory
```python run_pretrained_interactive.py```
6. Every Python script available allows you to change various settings. For example see:
```python run_pretrained_interactive.py -h```

By default, the game will terminate after 32K steps, or ~1 hour. You can increase this by adjusting `--max_steps` from the command line, but it will also use more memory. 

Interact with the emulator using the arrow keys and the `a` and `s` keys (A and B buttons).  
You can pause the AI's input during the game by editing `agent_enabled.txt` from 'yes' to 'no'.

Note: the `PokemonRed.gb` file MUST be in the main directory.
Your current directory MUST be the `src/baselines/` directory in order to run any Python scripts.

## Training the Model 🏋️ 
Note: By default this can use up to ~100G of RAM. You can decrease this by:

a) Lowering `--cpu_count` from the command line when calling the script.

b) Lowering `--max_steps` from the command line when calling the script.

Setting these to lower than their defaults may affect the results. Also, the model behavior may become degenerate for up to the first 50 training iterations or so before starting to improve. This could likely be fixed with better hyperparameters, but I haven't had the time or resources to sweep these.

1. Previous steps 1-3
2. From main directory, run `parallel_tutorial`
3. Or, 
Go to `src/baselines/` and run ```python run_baseline_parallel.py```


## Tracking Training Progress 📈 

You can view the current state of each emulator, plot basic stats, and compare to previous runs using the `VisualizeProgress.ipynb` notebook.

## Extra 🐜
Map visualization code can be found in `src/visualization/` directory.
