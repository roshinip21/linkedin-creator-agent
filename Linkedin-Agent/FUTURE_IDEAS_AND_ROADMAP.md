# 🚀 LinkPulse AI — LinkedIn Creator & Network Agent
## Future Ideas, Architecture & Roadmap

### 📋 Overview
**LinkPulse AI** is an intelligent assistant designed specifically for Bay Area founders, engineers, and creators. It streamlines content ideation, drafts human-like comments without AI clichés or em-dashes, acts as a high-priority DM concierge, and tracks local creator meetups and workshops.

---

### 🌟 Implemented Capabilities (Live in Repo)

1. **Trending Tech Content Ideation (`fetch_trending_topics`, `draft_post_idea`)**:
   - Analyzes real-time topics across the Bay Area (Autonomous Coding Agents, Edge AI hardware, Open Source vs. API economics).
   - Generates hooks, multi-slide carousel outlines, and visual generation prompts for **Nano Banana 2 Lite** (`gemini-3.1-flash-lite-image`).

2. **Persistent Visual Asset & Slide Deck Storage (`store_and_publish_visual_asset`)**:
   - Automatically publishes generated carousel layout specs, banner graphics, and infographic structures to **Google Cloud Storage** (`gs://bwg3-qwiklabs-gcp-04-a0c213e22c19/generated_content/`).
   - Generates public URLs directly accessible in browser or via API.

3. **Human-in-the-Loop Peer Commenting (`draft_friend_comment`)**:
   - Strict style guardrail: **Zero em-dashes (`—`)** and no generic corporate fluff.
   - Outputs conversational options held under `PENDING_USER_APPROVAL` so nothing is ever posted without user confirmation.

4. **Direct Message Concierge (`summarize_direct_messages`)**:
   - Parses simulated or connected LinkedIn messages to surface urgent opportunities (recruiter reachouts, private founder dinners, press quotes).

5. **Bay Area Creator Radar (`monitor_bay_area_creator_events`)**:
   - Tracks upcoming hackathons, AI builder workshops, and creator meetups across SF, Mountain View, and Palo Alto with RSVP links.

6. **Web Presentation UI & Recorded Demo**:
   - Interactive chat frontend located in `frontend/`.
   - Screen-recorded demo video with branded frame: `linkpulse_demo.webm`.

---

### 🔮 Future Ideas & Roadmap

#### 1. Live LinkedIn API Integration
- Connect LinkedIn Official Community Management / Share APIs or a secure headless browser session to publish approved posts directly.
- Read inbound inbox messages in real time instead of simulated batches.

#### 2. Native Multi-Image Carousel Generation
- Automatically render SVG or PNG slides with customized fonts and brand themes from the carousel specs.
- Convert multi-slide decks directly into LinkedIn PDF document carousels (which receive the highest organic reach on LinkedIn).

#### 3. Cross-Session Long-Term Memory (Vertex AI Memory Bank)
- Wire Vertex AI Memory Bank to retain user preferences over time:
  - Personal tone (e.g. casual engineer, formal executive, technical builder).
  - List of close friends and VIP connections to prioritize.
  - History of topics already posted to avoid repetition.

#### 4. Automated Recurring Cron Job (`/schedule`)
- Trigger a daily 8:00 AM PST digest of priority DMs and trending news.
- Trigger a weekly Sunday evening ideation session to plan 3 posts for the upcoming week.

#### 5. Video Scripting & Generation
- Expand `draft_post_idea` to output 60-second vertical video scripts with b-roll suggestions, teleprompter text, and audio prompts for short-form clips (LinkedIn Video, TikTok, Reels).
