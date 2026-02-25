# ContentSwarm

ContentSwarm is an AI-powered content processing platform that automates the creation and scheduling of social media content across multiple platforms including TikTok, Instagram Reels, and YouTube Shorts.

## Features

- Automated content creation from source URLs
- Multi-platform content scheduling
- AI-powered caption generation
- Thumbnail generation using local vision models
- RESTful API for integration

## Architecture

ContentSwarm uses a swarm-based architecture where different agents handle specific tasks:

1. **Content Extraction Agent** - Extracts content from source URLs
2. **Content Processing Agent** - Processes and formats content for different platforms
3. **Caption Generation Agent** - Generates platform-specific captions
4. **Thumbnail Agent** - Creates platform-optimized thumbnails
5. **Scheduling Agent** - Schedules content based on posting schedules

## Getting Started

### Prerequisites

- Python 3.11+
- Docker (for containerized deployment)

### Installation

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
# Run with uvicorn
uvicorn src.api:app --host 0.0.0.0 --port 8000

# Or with Docker
sudo docker build -t contentswarm .
sudo docker run -p 8000:8000 contentswarm
```

## API Endpoints

- `POST /process` - Process content from URL
- `GET /health` - Health check endpoint

## Configuration

Configuration is managed through `config.yaml`:

```yaml
brand_voice: "Engaging, informative, and conversational tone with a focus on storytelling"
posting_schedules:
  tiktok:
    monday: "09:00"
    tuesday: "14:00"
    wednesday: "11:00"
    thursday: "16:00"
    friday: "10:00"
  reels:
    monday: "10:00"
    tuesday: "15:00"
    wednesday: "12:00"
    thursday: "17:00"
    friday: "11:00"
  shorts:
    monday: "08:00"
    tuesday: "13:00"
    wednesday: "09:00"
    thursday: "14:00"
    friday: "07:00"
platform_tokens:
  tiktok: "tiktok_api_token"
  reels: "reels_api_token"
  shorts: "shorts_api_token"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Contact

For support or questions, please open an issue on GitHub.
