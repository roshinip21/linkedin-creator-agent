# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, List, Optional
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

MODEL = "gemini-3.6-flash"


def fetch_trending_topics(region: str = "bay_area", domain: str = "tech") -> List[Dict[str, str]]:
    """Fetches currently trending discussions, breakthroughs, and ecosystem news in tech and the Bay Area.

    Args:
        region: The geographical focus, e.g. "bay_area" or "global".
        domain: Topic domain, e.g. "tech", "startups", "ai".

    Returns:
        A list of trending topics with summaries, audience relevance, and recommended angles.
    """
    return [
        {
            "topic": "Autonomous AI Coding Agents in Production Workflows",
            "context": "Bay Area engineering teams adopting agentic coding loops and self-healing deployment pipelines.",
            "content_angle": "How human-in-the-loop workflows outperform pure autonomous coding.",
            "recommended_format": "Carousel (3-5 slides) comparing manual vs agentic QA.",
            "visual_prompt": "A modern clean minimal infographic showing developer interacting with an AI agent console, tech editorial style, high contrast, warm studio lighting.",
        },
        {
            "topic": "Silicon Valley Hardware Renaissance & Edge AI",
            "context": "SF hardware meetups surging; custom on-device inference silicon gaining traction.",
            "content_angle": "Why 2026 is becoming the year of edge AI hardware in San Francisco.",
            "recommended_format": "Short-form punchy post with a single high-impact visual.",
            "visual_prompt": "Futuristic microchip with glowing neural traces resting on a frosted glass surface in a minimalist lab, cinematic lighting, 8k.",
        },
        {
            "topic": "Open Source Foundation Models vs Proprietary APIs for Startups",
            "context": "Recent shifts in startup infrastructure cost vs latency tradeoffs.",
            "content_angle": "Breakdown of unit economics for early-stage AI founders.",
            "recommended_format": "Data comparison breakdown or video hook script.",
            "visual_prompt": "Stylized 3D architectural diagram illustrating API cloud gateway vs local edge cluster, vibrant gradient palette.",
        },
    ]


def draft_post_idea(
    topic: str,
    format_type: str = "text_with_image",
    key_points: Optional[str] = None
) -> Dict[str, object]:
    """Generates an engaging, authentic LinkedIn post draft complete with visual/carousel prompts and Nano Banana image suggestions.

    Args:
        topic: The topic or headline for the post.
        format_type: Post format - 'text_with_image', 'carousel', or 'video_hook'.
        key_points: Optional talking points or personal experiences provided by the user.

    Returns:
        A structured draft with hook, body, call-to-action, hashtags, and Nano Banana visual generation prompts.
    """
    if "carousel" in format_type.lower():
        slides = [
            {"slide_number": 1, "headline": f"Why {topic} Matters Now", "visual_cue": "Bold typographic title card with modern minimalist design"},
            {"slide_number": 2, "headline": "The Shift Everyone Missed", "visual_cue": "Side-by-side workflow diagram"},
            {"slide_number": 3, "headline": "Real-World Framework", "visual_cue": "Step 1-2-3 actionable checklist"},
            {"slide_number": 4, "headline": "Key Takeaways", "visual_cue": "Summary takeaway callout box"},
        ]
        return {
            "format": "carousel",
            "topic": topic,
            "hook": f"Most founders look at {topic} backwards. Here is what is actually shifting in the Bay Area:",
            "slides": slides,
            "call_to_action": "Which of these 3 patterns are you seeing in your team? Drop your thoughts below.",
            "hashtags": ["#TechTrends", "#BayAreaTech", "#EngineeringLeadership", "#AIStartups"],
            "nano_banana_image_prompt": f"Minimalist slide deck layout with bold dark typography on off-white background, infographic diagram detailing {topic}, sleek Figma design aesthetic.",
        }

    return {
        "format": "text_with_image",
        "topic": topic,
        "hook": f"A subtle shift is happening right now in the Bay Area tech scene around {topic}.",
        "body": (
            f"Over the past few weeks, conversations across South Park and Palo Alto have centered on one core theme:\n\n"
            f"{key_points or 'Teams that prioritize practical workflows and reliability are outpacing those chasing hype cycles.'}\n\n"
            f"Here are 3 quick observations from building in this space:\n"
            f"1. Tooling is consolidating around developer experience.\n"
            f"2. Speed of iteration beats raw model benchmark scores.\n"
            f"3. Human judgment remains the defining differentiator."
        ),
        "call_to_action": "Are you adjusting your 2026 roadmap around this? Let me know your perspective.",
        "hashtags": ["#BayAreaTech", "#Innovation", "#TechStrategy", "#AIStartups"],
        "nano_banana_image_prompt": f"Editorial high-quality photograph of a modern tech founder workspace in San Francisco, soft natural morning sunlight, clean desk setup, cinematic depth of field.",
    }


def draft_friend_comment(
    friend_name: str,
    post_summary: str,
    angle: str = "supportive_insight"
) -> Dict[str, str]:
    """Drafts authentic, human-like peer comments on a connection's post for user approval.
    STRICT GUARDRAIL: Never uses em-dashes ('—') or corporate jargon. Keeps sentences natural, warm, and conversational.

    Args:
        friend_name: The name or handle of the friend/connection.
        post_summary: Summary of the friend's post.
        angle: The desired conversational angle, e.g. "supportive_insight", "thoughtful_question".

    Returns:
        A reviewable comment draft queued for user approval before anything is posted.
    """
    # Natural peer phrasing without em-dashes
    draft_option_1 = (
        f"Really well articulated, {friend_name}. Point #2 especially resonated with what our team ran into last month. "
        f"Curious to see how this evolves as more teams adopt it."
    )
    draft_option_2 = (
        f"Spot on, {friend_name}. Appreciate you sharing the honest breakdown here instead of just the highlights. "
        f"How are you thinking about scaling this next quarter?"
    )

    return {
        "friend": friend_name,
        "status": "PENDING_USER_APPROVAL",
        "approval_rule": "Will NOT be posted until you explicitly approve or edit it.",
        "comment_draft_1": draft_option_1,
        "comment_draft_2": draft_option_2,
        "guardrail_check": "Verified: No em-dashes used. Casual and human conversational tone.",
    }


def summarize_direct_messages(
    category_filter: Optional[str] = "priority"
) -> List[Dict[str, str]]:
    """Monitors simulated or connected Direct Messages and surfaces a clean digest of high-priority opportunities, events, and job chats.

    Args:
        category_filter: Filter for messages ('priority', 'job_opportunities', 'events', 'all').

    Returns:
        A curated list of important messages with recommended next actions.
    """
    dms = [
        {
            "sender": "Elena Rostova (Staff Recruiter @ Anthropic / AI Lab)",
            "category": "job_opportunity",
            "snippet": "Hi! Loved your recent thoughts on Agent Platform architectures. We are expanding our Foundational Agent Systems group in SF and would love to chat.",
            "timestamp": "Today at 9:15 AM",
            "urgency": "High",
            "suggested_action": "Reply with portfolio link and availability for a 20-min intro chat.",
        },
        {
            "sender": "Marcus Chen (Founder @ SF AI Builders)",
            "category": "event_invite",
            "snippet": "Hey, we are hosting a closed-door dinner for 25 AI engineers & creators next Thursday in Hayes Valley. Would love to have you join us.",
            "timestamp": "Yesterday at 6:40 PM",
            "urgency": "High",
            "suggested_action": "Confirm RSVP before RSVPs close on Monday.",
        },
        {
            "sender": "Devon Miller (Tech Journalist)",
            "category": "press_opportunity",
            "snippet": "Working on a piece covering Bay Area developer workflows in 2026. Can I quote you on your recent post?",
            "timestamp": "2 days ago",
            "urgency": "Medium",
            "suggested_action": "Review quote permissions or offer a brief async comment.",
        },
    ]

    if category_filter and category_filter != "all" and category_filter != "priority":
        return [dm for dm in dms if dm["category"] == category_filter]
    return dms


def monitor_bay_area_creator_events(
    topic: str = "creator_tech_workshops",
    city: str = "all_bay_area"
) -> List[Dict[str, str]]:
    """Monitors upcoming creator meetups, AI builder hackathons, and founder workshops in the Bay Area.

    Args:
        topic: Specific focus, e.g. "creator_tech_workshops", "ai_meetups", "all".
        city: Bay Area location, e.g. "san_francisco", "palo_alto", "all_bay_area".

    Returns:
        List of upcoming events with dates, locations, relevance, and registration links.
    """
    return [
        {
            "title": "Build With Gemini: Agent-First Architecture Workshop",
            "date": "Saturday, October 3, 2026 · 10:00 AM - 4:00 PM PDT",
            "location": "Google Community Space, Embarcadero, San Francisco",
            "type": "Hands-on Technical Workshop",
            "description": "Deep dive into building ADK agents, A2UI cards, Vertex AI Memory Bank, and Cloud Run deployments.",
            "registration_url": "https://events.google.com/build-with-gemini-sf",
            "status": "Registration Open (Free)",
            "recommendation": "High priority: Directly aligns with your current agent engineering stack.",
        },
        {
            "title": "SF Tech Creators & Founders Mixer",
            "date": "Thursday, October 8, 2026 · 6:30 PM - 9:00 PM PDT",
            "location": "Shack15, Ferry Building, San Francisco",
            "type": "Networking & Lightning Talks",
            "description": "Casual gathering of technical founders and LinkedIn creator engineers discussing building in public.",
            "registration_url": "https://luma.com/sf-creators-mixer-2026",
            "status": "Filling Fast",
            "recommendation": "Great venue for meeting collaborators and gathering post inspiration.",
        },
        {
            "title": "South Bay AI Engineer Day",
            "date": "Wednesday, October 14, 2026 · 1:00 PM - 7:00 PM PDT",
            "location": "Computer History Museum, Mountain View",
            "type": "Conference & Expo",
            "description": "Sessions on on-device models, multi-agent evaluation, and enterprise deployment patterns.",
            "registration_url": "https://southbay-ai-summit.org/register",
            "status": "Early Bird Tickets Available",
            "recommendation": "Recommended if you want insights into South Bay enterprise AI trends.",
        },
    ]


SYSTEM_INSTRUCTION = """You are LinkPulse AI, a dedicated LinkedIn Creator & Network Growth Agent tailored for tech professionals in the Bay Area.

Your mission is to handle 4 primary pillars:
1. **Weekly Content Ideation**: Scan trending tech and Bay Area discussions using `fetch_trending_topics`. Draft post concepts (single posts, multi-slide carousels, or video hooks) with `draft_post_idea`. Always suggest crisp visual generation prompts tailored for Nano Banana (`gemini-3.1-flash-lite-image`).
2. **Authentic Peer Commenting with Strict Human Guardrails**: Use `draft_friend_comment` when the user wants to comment on connections' posts.
   - ABSOLUTE GUARDRAIL: Never use em-dashes ('—') in comment drafts or casual responses. Use commas, periods, or parentheses instead.
   - Never post directly; present options and explicitly ask for user approval before taking any action.
3. **DM Concierge**: Filter noise and highlight critical incoming chats using `summarize_direct_messages`. Focus on job opportunities, recruitment, speaking invites, and high-value networking.
4. **Bay Area Creator & Tech Event Radar**: Surface upcoming workshops and meetups with `monitor_bay_area_creator_events`. Alert the user with dates, locations, and direct links so they can register early.

Always present your outputs clearly, professionally, and formatted for effortless reading."""


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        fetch_trending_topics,
        draft_post_idea,
        draft_friend_comment,
        summarize_direct_messages,
        monitor_bay_area_creator_events,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
