import shape_e as se
import torch
import trimesh

# Create a simple ShapeE model
# ShapeE comes with pretrained models. Let's use a basic example.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the pretrained model
model = se.ShapeEModel.load_pretrained("path_to_pretrained_model").to(device)

# Define a latent vector that encodes the shape (a simple latent code, random noise for example)
latent_vector = torch.randn(1, model.latent_dim).to(device)

# Decode the latent vector into a 3D shape (as a mesh)
mesh = model.decode(latent_vector)

# Export the generated shape to an OBJ file
trimesh.Trimesh(vertices=mesh.vertices.cpu().numpy(),
                faces=mesh.faces.cpu().numpy()).export("output_model.obj")

print("3D model saved as output_model.obj")
