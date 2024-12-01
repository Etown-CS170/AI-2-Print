# --- Getting Shap-e and Slicing Algorithm Files ---
# git clone https://github.com/openai/shap-e
# git clone https://github.com/Nehri/slicing_algorithm.git
# cd /content/shap-e/
# pip install -e .

# --- Python Packages to Install ---
# pip install numpy
# pip install torch

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
guidance_scale = 15.0
prompt = "baby grand piano" # area for user to type text prompt for mesh generation

latents = sample_latents(
    batch_size=batch_size,
    model=model,
    diffusion=diffusion,
    guidance_scale=guidance_scale,
    model_kwargs=dict(texts=[prompt] * batch_size),
    progress=True,
    clip_denoised=True,
    use_fp16=True,
    use_karras=True,
    karras_steps=20, # this sets the amount of noise in processing the mesh
    sigma_min=1e-3,
    sigma_max=160,
    s_churn=0,
)

for i, latent in enumerate(latents):
    t = decode_latent_mesh(xm, latent).tri_mesh()
    with open(f'mesh_{i}.obj', 'w') as f:
        t.write_obj(f)