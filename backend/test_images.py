import asyncio
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent / "backend"))

async def test_image_generation():
    """Quick test to debug image generation."""
    print("🔍 Testing Image Generation Pipeline...\n")
    
    try:
        # Test 1: Check imports
        print("✓ Step 1: Checking imports...")
        from agents.image_agent import generate_image
        from services.image_service import generate_car_image
        print("  ✅ Imports successful\n")
        
        # Test 2: Check environment
        print("✓ Step 2: Checking environment...")
        from config import get_settings
        settings = get_settings()
        print(f"  - GROQ_API_KEY: {'✅ Set' if settings.groq_api_key else '❌ NOT SET'}")
        print(f"  - App Name: {settings.app_name}\n")
        
        # Test 3: Check image directory
        print("✓ Step 3: Checking image directory...")
        images_dir = Path("./database/generated_images")
        images_dir.mkdir(parents=True, exist_ok=True)
        print(f"  ✅ Images dir created: {images_dir.absolute()}\n")
        
        # Test 4: Generate a test image
        print("✓ Step 4: Generating test image...")
        prompt = "futuristic electric sports car"
        print(f"  Prompt: {prompt}")
        
        try:
            image_filename = await generate_image(prompt, style="photorealistic")
            print(f"  ✅ Image generated: {image_filename}")
            
            # Check if file exists
            image_path = images_dir / image_filename
            if image_path.exists():
                file_size = image_path.stat().st_size
                print(f"  ✅ File exists: {image_path}")
                print(f"  ✅ File size: {file_size / 1024:.1f} KB\n")
            else:
                print(f"  ❌ File not found: {image_path}\n")
                
        except Exception as e:
            print(f"  ❌ Image generation failed: {str(e)}\n")
            import traceback
            traceback.print_exc()
        
        # Test 5: Check full pipeline
        print("✓ Step 5: Testing full report generation...")
        from agents.orchestrator import generate_full_report
        
        try:
            result = await generate_full_report("Design a futuristic electric SUV for Indian market")
            print(f"  ✅ Report ID: {result['report_id']}")
            print(f"  ✅ Image URL: {result.get('image_url', 'NOT SET')}")
            print(f"  ✅ Image Filename: {result.get('image_filename', 'NOT SET')}\n")
        except Exception as e:
            print(f"  ❌ Full pipeline failed: {str(e)}\n")
            import traceback
            traceback.print_exc()
            
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_image_generation())
