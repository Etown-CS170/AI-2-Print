# A majority of this code in this file was included in the Shap-e

# --- Getting Shap-e and Slicing Algorithm Files ---
# git clone https://github.com/openai/shap-e
# git clone https://github.com/Nehri/slicing_algorithm.git
# cd /content/shap-e/
# pip install -e .

# --- Python Packages Needed ---

# pip install numpy # this is a library that deals with computation
# pip install torch # this is the library that deals with the machine learning computation

import torch
import pymeshlab
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import decode_latent_mesh
from shap_e.util.notebooks import create_pan_cameras, decode_latent_images, gif_widget


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') # This line sets torch to use a GPU for much faster processing

xm = load_model('transmitter', device=device)
model = load_model('text300M', device=device)
diffusion = diffusion_from_config(load_config('diffusion'))

batch_size = 1 
guidance_scale = 15.0  # this determines the freedom of the prompt, higher number means more accurate to the description
prompt = "baby grand piano" # area for user to type text prompt for mesh generation

latents = sample_latents(
    batch_size=batch_size,
    model=model,
    diffusion=diffusion,
    guidance_scale=guidance_scale, 
    model_kwargs=dict(texts=[prompt] * batch_size),
    progress=True, # shows user how far along the process is "In this case a progress bar"
    clip_denoised=True, # this important to get rid of numbers outside range for usable outputs
    use_fp16=True, # this sets the model to use 16-bit floating point precision when the model does computations
    use_karras=True, # enables the model to use karras steps
    karras_steps=20, # this sets the amount of noise in processing the mesh
    sigma_min=1e-3, # this sets the minimum amount of noise the model can use when sampling
    sigma_max=160, # this the same but for the maximum
    s_churn=0, # controls the level of variability in the sampling process which can diversify the "creativity" of the outputs
)

# --- this code decodes latents into a mesh, and then writes the meshes data to an OBJ file ---
for i, latent in enumerate(latents):
    t = decode_latent_mesh(xm, latent).tri_mesh()
    with open(f'mesh_{i}.obj', 'w') as f:
        t.write_obj(f)