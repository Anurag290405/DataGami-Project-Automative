import asyncio
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

async def test_image_only():
    """Test ONLY image generation without chromadb dependency."""
    print("Testing Image Generation Only...\n")
    
    try:
        # Test 1: Check image service directly
        print("Step 1: Testing image service...")
        from services.image_service import generate_vehicle_image, get_image_url
        print("  Image service imported\n")
        
        # Test 2: Check image directory
        print("Step 2: Checking image directory...")
        images_dir = Path("./database/generated_images")
        images_dir.mkdir(parents=True, exist_ok=True)
        print(f"  Images dir: {images_dir.absolute()}\n")
        
        # Test 3: Generate a test image
        print("Step 3: Generating test image via thread...")
        prompt = "futuristic concept electric SUV with LED headlights"
        print(f"  Prompt: {prompt}")
        print("  This may take 30-60 seconds...\n")
        
        try:
            # Run the blocking function in thread pool
            filename = await asyncio.to_thread(generate_vehicle_image, prompt, "photorealistic")
            print(f"  Filename returned: {filename}\n")
            
            # Check if file exists
            image_path = images_dir / filename
            if image_path.exists():
                file_size = image_path.stat().st_size
                print(f"  File exists: {image_path}")
                print(f"  File size: {file_size / 1024:.1f} KB")
                
                # Get URL
                image_url = get_image_url(filename)
                print(f"  Public URL: {image_url}\n")
                
                print("IMAGE GENERATION SUCCESSFUL!")
                return True
            else:
                print(f"  File not found: {image_path}\n")
                return False
                
        except Exception as e:
            print(f"  Generation failed: {str(e)}\n")
            import traceback
            traceback.print_exc()
            return False
            
    except Exception as e:
        print(f"Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_image_only())
    sys.exit(0 if success else 1)
