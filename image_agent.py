from diffusers import StableDiffusionPipeline
import torch
import os

class ImageAgent:

    def __init__(self, llm):
        self.llm = llm

        # -------- LOAD FAST MODEL --------
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "stabilityai/sd-turbo",
            torch_dtype=torch.float32
        )

        self.pipe = self.pipe.to("cpu")

        # Speed optimization
        self.pipe.enable_attention_slicing()

    # -------- PROMPT ENHANCEMENT --------
    def enhance_prompt(self, user_prompt):
        prompt = f"""
Enhance this image prompt for Stable Diffusion.

Add:
- cinematic lighting
- ultra realistic details
- sharp focus
- 4k quality

User input: {user_prompt}

Return ONLY the enhanced prompt.
"""
        try:
            return self.llm.call(prompt).strip()
        except:
            return user_prompt  # fallback

    # -------- IMAGE GENERATION --------
    def generate(self, user_prompt):

        enhanced_prompt = self.enhance_prompt(user_prompt)

        negative_prompt = (
            "blurry, low quality, bad anatomy, extra limbs, distorted, "
            "watermark, text, signature, ugly, deformed, noisy"
        )

        try:
            image = self.pipe(
                prompt=enhanced_prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=20,   # fast + good
                guidance_scale=6.5,      # better quality
                height=512,
                width=512
            ).images[0]

        except Exception as e:
            print("⚠️ Error:", e)

            # fallback simple generation
            image = self.pipe(
                prompt=user_prompt,
                num_inference_steps=15,
                guidance_scale=5.0,
                height=256,
                width=256
            ).images[0]

        # -------- SAVE IMAGE --------
        os.makedirs("static", exist_ok=True)

        path = "static/generated.png"
        image.save(path)

        return path
