# My agent: LinkedIn Creator & Network Agent (LinkPulse AI)

One-liner: A conversational agent that helps tech professionals and creators in the Bay Area ideate trending multi-format posts with Nano Banana visual prompts, draft human-like engagement comments without em-dashes for approval, monitor and summarize high-value DMs, and track local creator events/workshops.

Use Cases & Features:
1. **Weekly Content Ideator**: Scans trending tech topics and Bay Area industry news to propose post angles. Formats drafts for carousels, text posts, and prompts image generation via Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`) or video concepts.
2. **Engagement & Friend Post Commenter**: Generates genuine, conversational comments tailored to peers' posts. Strict guardrail: zero em-dashes ("—"), natural phrasing, queued for user review & explicit approval before posting.
3. **Direct Message Concierge**: Analyzes inbox messages, filtering noise and surfacing a priority digest for job opportunities, recruitment, and networking invites.
4. **Bay Area Creator Event Radar**: Tracks upcoming workshops, meetups, and creator events in the Bay Area, generating rich event cards and prompting the user to RSVP/register.

Tool coverage:
- **Memory**: Remembers user profile/domain preferences, writing tone/voice rules (no em-dashes), connection list, and past posted topics to prevent repetition.
- **Tools**: 
  - `fetch_trending_tech_topics(region="bay_area", domain="tech")`
  - `draft_post_content(topic, format, prompt_visuals=True)`
  - `draft_comment(post_text, author, tone="conversational_peer")`
  - `summarize_dms(filter_categories=["job_opportunity", "event_invite"])`
  - `find_bay_area_events(category="creator_workshop")`
  - `generate_post_visual(prompt)` (Nano Banana 2 Lite / Imagen)
- **Catalog/UI**: Event schedule cards, post drafts, and DM summary digests formatted with A2UI cards/tables.
- **Image gen**: Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`) for infographics, carousel slide visuals, and post banners.
- **Sandbox**: Can be used to parse/filter incoming DM metrics, format carousel slide decks, or compute engagement analytics.

Recommended for every project: memory, storage (Firestore for tracking posts & drafts), tools, image generation (Nano Banana), A2UI cards.
Agent-specific / stretch (pick what fits): Video generation concepts with Omni, LinkedIn API integration or mock fixtures, code execution for carousel data layout.
