import re
import json

# Complete slide-by-slide English presentation guide tailored for a Digital Twin & Data Engineer interview/assignment.
# Starts directly with the client project (no personal self-intro), reflecting the real engagement workflow:
# Client came to our office -> wanted automation & Digital Twin -> we visited industry -> built blueprint ->
# 3-developer core team (~40-50% backend contribution by the presenter).
# Every tricky, multi-syllable, or technical English word includes Bengali pronunciation in brackets.
guide_text = """================================================================================
AUTOTASKX — ENGLISH TECHNICAL PRESENTATION & INTERVIEW MASTER GUIDE
================================================================================
Target Role: Digital Twin & Data Engineer
Project: AutoTaskX — Industrial IoT & Real-Time Digital Twin Platform
Client: A Prominent Player in the Bangladeshi Textile Industry
Team & Contribution: 3-Developer Core Team (Backend & Frontend) · One of the Main Backend Engineers (~40–50% of total work)
Workflow: Office Consultation → Industry Visit → Requirements & Blueprint → 4-Month Live Delivery (24/7)
================================================================================

[পড়ার এবং প্রেজেন্ট করার সহজ টিপস — How to Deliver Smoothly]
--------------------------------------------------------------------------------
• আপনি যেহেতু আগেই নিজের পরিচয় দিয়ে দিয়েছেন, তাই এখানে কোনো Self-Introduction (নিজের পরিচয়) রাখা হয়নি — সরাসরি প্রজেক্ট এবং ক্লায়েন্টের গল্প দিয়ে শুরু করা হয়েছে।
• প্রজেক্টটি ৩ জন ডেভেলপারের একটি কোর টিমের (Core Developer Team) কাজ — Backend ও Frontend মিলে। আপনি এই কোর টিমের একজন মূল Backend Engineer হিসেবে প্রায় ৪০–৫০% কাজ করেছেন; তাই সব জায়গায় "I built" না বলে "We built / We created" ব্যবহার করা হয়েছে।
• প্রতিটি স্লাইড সাজানো হয়েছে ক্লায়েন্টের বাস্তব চাহিদা অনুযায়ী: Client Request / Problem → Factory Visit & Solution → Result।
• কঠিন ও টেকনিক্যাল ইংরেজি শব্দগুলোর ঠিক পাশেই ব্র্যাকেটে বাংলা উচ্চারণ দেওয়া আছে, যেন আপনি লেখা দেখে সাবলীলভাবে পড়তে পারেন।
• বলার সময় "To be honest...", "You know...", "Basically...", "What the client really wanted..." এই কথাগুলো স্বাভাবিকভাবে বলে যাবেন।

================================================================================
SLIDE 01: PROJECT OVERVIEW & CLIENT VISION (প্রজেক্ট পরিচিতি ও ক্লায়েন্টের ভিশন)
[পিলার: Client Vision & Project Objectives]
================================================================================
স্লাইডের উদ্দেশ্য:
নিজের পরিচয় না দিয়ে সরাসরি প্রজেক্ট দিয়ে শুরু করা — কীভাবে বাংলাদেশের একটি বড় টেক্সটাইল ক্লায়েন্ট আমাদের অফিসে এসে অটোমেশন ও ডিজিটাল টুইন চেয়েছিলেন, ইন্ডাস্ট্রি ভিজিটের পর আমরা পুরো আর্কিটেকচার দাঁড় করাই এবং ৩ জনের টিমে আপনার ৪০-৫০% ব্যাকএন্ড অবদান তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Let's jump straight into the project — AutoTaskX (অটো-টাস্ক-এক্স). Basically (বেসিক্যালি), it's an Industrial IoT (ইন্ডাস্ট্রিয়াল আই-ও-টি) and real-time (রিয়েল-টাইম) Digital Twin (ডিজিটাল টুইন) platform (প্ল্যাটফর্ম) built for one of the most prominent (প্রমিনেন্ট) players in the Bangladeshi textile industry (ইন্ডাস্ট্রি).

▶ How It Started (The Client Request):
To be honest (টু বি অনেস্ট), this project (প্রজেক্ট) started in a very interesting (ইন্টারেস্টিং) way. The client (ক্লায়েন্ট) had already identified (আইডেন্টিফাইড) major (মেজর) gaps in their operations (অপারেশনস) and actually (অ্যাকচুয়ালি) walked into our company's (কোম্পানিজ) office. What they really wanted was full automation (অটোমেশন) of their factory system (সিস্টেম) — essentially (এসেনশিয়ালি) converting (কনভার্টিং) their entire (এনটায়ার) production (প্রোডাকশন) floor into a live Digital Twin (ডিজিটাল টুইন).

▶ Discovery (ডিসকভারি) & Our Solution (সলিউশন):
Right after that office discussion (ডিসকাশন), our team visited their factory to inspect (ইন্সপেক্ট) the physical (ফিজিক্যাল) machinery (মেশিনারি), you know, dyeing (ডাইং) jets, stenters (স্টেন্টার), and lab equipment (ইকুইপমেন্ট). From there, we organized (অর্গানাইজড) the complete (কমপ্লিট) requirements (রিকোয়ারমেন্টস) and created (ক্রিয়েটেড) the full software (সফটওয়্যার) architecture (আর্কিটেকচার) blueprint (ব্লুপ্রিন্ট). Over four months, a core team of three developers (ডেভেলপারস) — covering (কভারিং) both the backend (ব্যাকএন্ড) and frontend (ফ্রন্টএন্ড) — built the entire (এনটায়ার) system (সিস্টেম). I was one of the main engineers (ইঞ্জিনিয়ার্স) on the backend (ব্যাকএন্ড) system, handling (হ্যান্ডলিং) roughly (রাফলি) 40 to 50 percent (পারসেন্ট) of the total work — especially (এস্পেশালি) around the MQTT (এম-কিউ-টি-টি) Data Pipeline (ডাটা পাইপলাইন), Digital Twin (ডিজিটাল টুইন) synchronization (সিঙ্ক্রোনাইজেশন), and AI automation (এ-আই অটোমেশন) services (সার্ভিসেস).

▶ The Result (রেজাল্ট):
If you look at the right side of the slide, that's our live Digital Twin HUD (এইচ-ইউ-ডি). Every machine's state updates (আপডেটস) in under 25 milliseconds (মিলিসেকেন্ড), and the platform (প্ল্যাটফর্ম) is running 24/7 in live production (প্রোডাকশন) today."

--------------------------------------------------------------------------------
SLIDE 02: CLIENT PAIN POINTS & MILL REALITY (ক্লায়েন্টের সমস্যা ও ফ্যাক্টরি ভিজিটের অভিজ্ঞতা)
[পিলার: Problem Identification & Requirements]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্ট অফিসে এসে কী কী সমস্যার কথা বলেছিলেন এবং ইন্ডাস্ট্রি ভিজিটে গিয়ে আমরা কী দেখেছি তা পরিষ্কারভাবে তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"When the client (ক্লায়েন্ট) first came to our office, they walked us through the pain points slowing down their mill. And then, when we visited their factory floor to finalize (ফাইনালাইজ) our requirements (রিকোয়ারমেন্টস), we saw four major (মেজর) bottlenecks (বটলনেক) up close:

First, too much manual (ম্যানুয়াল) work. Lab technicians (টেকনিশিয়ান) were calculating (ক্যালকুলেটিং) dye formulas (ফর্মুলা) by hand, and supervisors (সুপারভাইজার) were writing machine readings (রিডিংস) into paper notebooks. You know, that's slow and very prone (প্রোন) to human error (হিউম্যান এরর).

Second, disconnected (ডিসকানেক্টেড) machines (মেশিনস). Every machine worked like an isolated (আইসোলেটেড) island. If one chamber (চেম্বার) overheated (ওভারহিটেড), nobody in the next department (ডিপার্টমেন্ট) knew about it.

Third, missing live data. The client wanted real-time (রিয়েল-টাইম) visibility (ভিজিবিলিটি), whereas (হোয়্যারঅ্যাজ) back then, management (ম্যানেজমেন্ট) only got reports (রিপোর্টস) at the end of the shift (শিফট) or once a week.

And fourth, delayed (ডিলেইড) reaction (রিঅ্যাকশন) cost. By the time someone caught a shade mismatch (মিসম্যাচ) or fabric (ফ্যাব্রিক) burning, an entire (এনটায়ার) 10,000-meter batch (ব্যাচ) could already be ruined (রুয়িনড).

▶ What the Client Asked For:
So, the client wanted one clear goal: eliminate (এলিমিনেট) manual (ম্যানুয়াল) guesswork (গেস-ওয়ার্ক) and convert (কনভার্ট) their entire (এনটায়ার) floor into an automated (অটোমেটেড), data-driven (ডাটা-ড্রিভেন) Digital Twin (ডিজিটাল টুইন)."

--------------------------------------------------------------------------------
SLIDE 03: ARCHITECTURE BLUEPRINT & 5 MODULES (সফটওয়্যার ব্লুপ্রিন্ট ও পাঁচটি মডিউল)
[পিলার: Solution Blueprint & Modular Design]
================================================================================
স্লাইডের উদ্দেশ্য:
ইন্ডাস্ট্রি ভিজিটের পর আমরা যে ৫-মডিউলের সফটওয়্যার ব্লুপ্রিন্ট তৈরি করি তা সহজভাবে উপস্থাপন করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Once we finished the factory visit and locked down the requirements (রিকোয়ারমেন্টস), we created (ক্রিয়েটেড) a software (সফটওয়্যার) architecture (আর্কিটেকচার) blueprint (ব্লুপ্রিন্ট) that wouldn't force the client (ক্লায়েন্ট) to replace (রিপ্লেস) any expensive (এক্সপেন্সিভ) machinery (মেশিনারি). Since the client wanted complete (কমপ্লিট) automation (অটোমেশন), we designed (ডিজাইনড) five modular (মডিউলার) engines (ইঞ্জিনস) sharing one unified (ইউনিফাইড) data pipeline (ডাটা পাইপলাইন):

Number one, Color Formulation (কালার ফর্মুলেশন) — which automates (অটোমেটস) lab dye math instead (ইনস্টেড) of trial-and-error (ট্রায়াল-অ্যান্ড-এরর).
Number two, Visual (ভিজ্যুয়াল) Quality (কোয়ালিটি) Inspection (ইন্সপেকশন) — using cameras (ক্যামেরাস) and AI automation (এ-আই অটোমেশন) to catch fabric defects (ডিফেক্ট) immediately (ইমিডিয়েটলি).
Number three, Production (প্রোডাকশন) Intelligence (ইন্টেলিজেন্স) — tracking (ট্র্যাকিং) machine runtime (রানটাইম), OEE (ও-ই-ই), and heat anomalies (অ্যানোমালিস).
Number four, Textile OS & Digital Twin (টেক্সটাইল ও-এস অ্যান্ড ডিজিটাল টুইন) — which connects (কানেক্টস) physical (ফিজিক্যাল) PLCs (পি-এল-সি) and sensors (সেন্সর) to maintain (মেইনটেইন) a live virtual (ভার্চুয়াল) copy of every machine.
And number five, ERP Integration (ই-আর-পি ইন্টিগ্রেশন) — syncing (সিঙ্কিং) shopfloor (শপফ্লোর) output directly (ডিরেক্টলি) with SAP (এস-এ-পি) or Datatex (ডাটাটেক্স).

You know, the beauty (বিউটি) of this blueprint (ব্লুপ্রিন্ট) is that every department (ডিপার্টমেন্ট) gets what the client asked for, while everything stays synchronized (সিঙ্ক্রোনাইজড) underneath (আন্ডারনিথ)."

--------------------------------------------------------------------------------
SLIDE 04: END-TO-END DATA PIPELINE (সেন্সর থেকে ড্যাশবোর্ডে ডাটা যাত্রা)
[পিলার: Data Engineering & MQTT Pipeline]
================================================================================
স্লাইডের উদ্দেশ্য:
ব্লুপ্রিন্ট অনুযায়ী ৪-ধাপের ডাটা পাইপলাইন (Sense → Connect → Process → Deliver) সহজ ও স্মার্টভাবে ব্যাখ্যা করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Inside our software (সফটওয়্যার) blueprint (ব্লুপ্রিন্ট), the backbone (ব্যাকবোন) of the whole Digital Twin (ডিজিটাল টুইন) is the end-to-end Data Pipeline (ডাটা পাইপলাইন). Let me break it down into four simple steps:

Step one is Sense (সেন্স) — industrial (ইন্ডাস্ট্রিয়াল) sensors (সেন্সর) like PT100 (পি-টি হান্ড্রেড) temperature (টেম্পারেচার) probes (প্রোব) and 16K line-scan (লাইন-স্ক্যান) cameras capture (ক্যাপচার) raw physical (ফিজিক্যাল) signals (সিগন্যালস) right from the client's machines.

Step two is Connect (কানেক্ট) — our local Edge Gateway (এজ গেটওয়ে) cleans that raw signal (সিগন্যাল) into standard (স্ট্যান্ডার্ড) JSON (জে-সন) format (ফরম্যাট) and pushes (পুশেস) it over MQTT (এম-কিউ-টি-টি) to our EMQX Broker (ই-এম-কিউ-এক্স ব্রোকার).

Step three is Process (প্রসেস) — our FastAPI (ফাস্ট-এ-পি-আই) backend (ব্যাকএন্ড) receives (রিসিভস) the MQTT (এম-কিউ-টি-টি) stream (স্ট্রিম), validates (ভ্যালিডেটস) the data, updates (আপডেটস) the live Digital Twin (ডিজিটাল টুইন) state, and stores the history (হিস্ট্রি) in TimescaleDB (টাইম-স্কেল-ডি-বি).

Step four is Deliver (ডেলিভার) — WebSockets (ওয়েব-সকেট) immediately (ইমিডিয়েটলি) push those live updates (আপডেটস) to the Next.js (নেক্সট-জে-এস) dashboard (ড্যাশবোর্ড).

To be honest (টু বি অনেস্ট), from a sensor (সেন্সর) reading (রিডিং) changing (চেঞ্জিং) on the floor to the client seeing it on screen — the whole journey (জার্নি) takes less than 25 milliseconds (মিলিসেকেন্ড)."

--------------------------------------------------------------------------------
SLIDE 05: FEATURE 01 — COLOR FORMULATION (স্মার্ট কালার ফর্মুলেশন)
[পিলার: Client Lab Automation]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের ডাইং ল্যাবের সমস্যা কীভাবে ম্যাথ ও অটোমেশন দিয়ে সমাধান করা হয়েছে তা বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Let's look at Feature (ফিচার) one — Color Formulation (কালার ফর্মুলেশন).

▶ What the Client Faced:
When we checked the client's dyeing (ডাইং) lab during our industry (ইন্ডাস্ট্রি) visit, matching (ম্যাচিং) a buyer's (বায়ার্স) color sample (স্যাম্পল) on the first try was honestly (অনেস্টলি) a huge bottleneck (বটলনেক). Chemists (কেমিস্ট) were spending 5 to 6 hours mixing and testing batches (ব্যাচেস) manually (ম্যানুয়ালি), wasting (ওয়েস্টিং) expensive (এক্সপেন্সিভ) dyes and water. The client specifically (স্পেসিফিক্যালি) asked us to automate (অটোমেট) this recipe (রেসিপি) process (প্রসেস).

▶ Our Solution (সলিউশন):
So we built a calculation (ক্যালকুলেশন) engine (ইঞ্জিন) using Kubelka-Munk (কুবেলকা-মাঙ্ক) optical (অপটিক্যাল) math. First, a Spectrophotometer (স্পেকট্রো-ফোটোমিটার) scans the target fabric (ফ্যাব্রিক) and reads its light wavelength (ওয়েভলেংথ). Then our engine calculates (ক্যালকুলেটস) the exact (এক্স্যাক্ট) grams of reactive (রিঅ্যাক্টিভ) dye needed per 100 kilograms (কিলোগ্রাম) and sends instructions (ইন্সট্রাকশনস) straight to the auto-dispenser (অটো-ডিস্পেন্সার). Of course, for safety, the lab still performs (পারফর্মস) a quick beaker (বিকার) validation (ভ্যালিডেশন) check before bulk production (প্রোডাকশন).

▶ The Result (রেজাল্ট):
Color variance (ভ্যারিয়েন্স) — known as Delta-E (ডেল্টা-ই) — stays under 1.0, which looks like an exact (এক্স্যাক্ট) match to the human eye, and first-pass lab success jumped to over 85 percent (পারসেন্ট)."

--------------------------------------------------------------------------------
SLIDE 06: FEATURE 02 — AI VISION INSPECTION (এ-আই ভিত্তিক কাপড়ের মান পরীক্ষা)
[পিলার: AI Automation & Quality Control]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের ফ্লোরে কাপড়ের ডিফেক্ট ধরতে AI Automation কীভাবে কাজ করে তা সহজ ভাষায় তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Moving on to Feature (ফিচার) two — Visual (ভিজ্যুয়াল) Quality (কোয়ালিটি) Inspection (ইন্সপেকশন) powered by AI automation (এ-আই অটোমেশন).

▶ What the Client Wanted:
Think about it — when fabric (ফ্যাব্রিক) moves at 80 to 120 meters per minute on a finishing (ফিনিশিং) machine, no human eye can reliably (রিলায়েবলি) catch tiny broken yarns (ইয়ার্নস) or oil spots under half a millimeter (মিলিমিটার). Plus, photos taken by floor staff on personal (পারসোনাল) phones used to get lost with zero audit (অডিট) trail (ট্রেইল). The client wanted an automated (অটোমেটেড) way to inspect (ইন্সপেক্ট) every meter and store proof cleanly.

▶ Our Solution (সলিউশন):
So, we integrated (ইন্টিগ্রেটেড) two camera inputs (ইনপুটস) into one unified (ইউনিফাইড) AI model (মডেল):
First, an industrial (ইন্ডাস্ট্রিয়াল) Basler (বাসলার) 16K line-scan (লাইন-স্ক্যান) camera mounted (মাউন্টেড) above the fabric line.
And second, a mobile app for floor auditors (অডিটর) to snap quick spot checks.

As frames (ফ্রেমস) come in, OpenCV (ওপেন-সি-ভি) buffers (বাফারস) the fabric strip, and our YOLO (ইয়োলো) vision (ভিশন) model automatically (অটোমেটিক্যালি) draws bounding boxes (বাউন্ডিং বক্সেস) around defects (ডিফেক্ট) smaller than 0.5 millimeters (মিলিমিটার) and classifies (ক্লাসিফাইস) each flaw (ফ্ল).

▶ The Result (রেজাল্ট):
Every single meter gets consistent (কনসিস্টেন্ট), automated (অটোমেটেড) inspection (ইন্সপেকশন) with a complete (কমপ্লিট) digital (ডিজিটাল) quality record (রেকর্ড)."

--------------------------------------------------------------------------------
SLIDE 07: KEY CHALLENGE & SOLUTION — IMAGE & DATA OFFLOADING (বড় ছবি বনাম সার্ভার স্পিড)
[পিলার: Data Engineering Deep Dive & System Design]
================================================================================
স্লাইডের উদ্দেশ্য:
২০ মেগাবাইটের ভারী ছবি আর ছোট সেন্সর ডাটা আলাদা রেখে আমরা কীভাবে সার্ভার ক্র্যাশ থেকে বাঁচিয়েছি তা দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Now, this slide is actually (অ্যাকচুয়ালি) a great engineering (ইঞ্জিনিয়ারিং) deep-dive (ডিপ-ডাইভ) from our architecture (আর্কিটেকচার) blueprint (ব্লুপ্রিন্ট), because it shows how we prevented (প্রিভেন্টেড) a serious (সিরিয়াস) data bottleneck (বটলনেক).

▶ The Technical (টেকনিক্যাল) Challenge (চ্যালেঞ্জ):
Each raw uncompressed (আনকম্প্রেসড) TIFF (টিফ) image (ইমেজ) coming off the 16K camera is around 20 megabytes (মেগাবাইট). To be honest (টু বি অনেস্ট), if we pushed 20-megabyte images every second through our FastAPI (ফাস্ট-এ-পি-আই) server (সার্ভার) or our MQTT Broker (এম-কিউ-টি-টি ব্রোকার), server memory (মেমোরি) and network bandwidth (ব্যান্ডউইথ) would crash within minutes.

▶ Our Solution (সলিউশন):
So, following (ফলোয়িং) this UML sequence (সিকোয়েন্স) diagram (ডায়াগ্রাম), we designed (ডিজাইনড) a parallel (প্যারালাল) offloading (অফলোডিং) pipeline (পাইপলাইন):
First, the Edge PC (এজ পি-সি) asks FastAPI (ফাস্ট-এ-পি-আই) for a temporary (টেম্পোরারি) Pre-signed S3 URL (প্রি-সাইনড এস-থ্রি ইউ-আর-এল).
Then, the Edge PC completely (কমপ্লিটলি) bypasses (বাইপাসেস) our API server and uploads (আপলোডস) that heavy 20-megabyte image directly (ডিরেক্টলি) to AWS S3 (এ-ডব্লিউ-এস এস-থ্রি).
At the exact (এক্স্যাক্ট) same moment, in parallel (প্যারালাল), the Edge PC sends only tiny scan metadata (মেটাডাটা) and AI defect (ডিফেক্ট) alerts (অ্যালার্টস) over MQTT (এম-কিউ-টি-টি).
FastAPI simply saves the image link in PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) and notifies (নোটিফাইস) the Next.js (নেক্সট-জে-এস) frontend (ফ্রন্টএন্ড) via WebSockets (ওয়েব-সকেট).

▶ The Result (রেজাল্ট):
Zero heavy file load on our backend (ব্যাকএন্ড), and zero memory (মেমোরি) bottlenecks (বটলনেক) even during peak production (প্রোডাকশন)."

--------------------------------------------------------------------------------
SLIDE 08: PRODUCTION INTELLIGENCE & AI ANOMALY ALERT (লাইভ মেশিন মনিটরিং ও দুর্ঘটনা রোধ)
[পিলার: Real-time Digital Twin & Safety Automation]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের চাহিদা অনুযায়ী রিয়েল-টাইম সেফটি মনিটরিং কীভাবে বড় ক্ষতি ঠেকায় তা বাস্তব উদাহরণ দিয়ে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Feature (ফিচার) three is Production Intelligence (ইন্টেলিজেন্স) — and this solves something the client was really worried (ওয়ারিড) about: catching machine issues (ইস্যুস) before fabric (ফ্যাব্রিক) gets ruined (রুয়িনড).

▶ The Real Floor Problem:
On a Stenter (স্টেন্টার) machine, the safe operating (অপারেটিং) limit for certain (সার্টেন) fabrics is 185 degrees (ডিগ্রিস) Celsius (সেলসিয়াস). If the chamber (চেম্বার) suddenly (সাডেনলি) spikes (স্পাইকস) to 192 degrees, the fabric can start burning or yellowing within minutes. Previously (প্রিভিয়াসলি), operators (অপারেটরস) only realized (রিয়েলাইজড) it after hundreds (হান্ড্রেডস) of meters were already damaged (ড্যামেজড).

▶ Our Solution (সলিউশন):
Because temperature (টেম্পারেচার) readings (রিডিংস) stream (স্ট্রিম) through MQTT (এম-কিউ-টি-টি) into our Digital Twin (ডিজিটাল টুইন) every second, the moment a sensor (সেন্সর) crosses 185 degrees and hits 192:
First, our anomaly detection (অ্যানোমালি ডিটেকশন) logic (লজিক) immediately (ইমিডিয়েটলি) highlights (হাইলাইটস) the machine in red on the dashboard (ড্যাশবোর্ড).
Second, an automated (অটোমেটেড) SMS alert (অ্যালার্ট) reaches the shift supervisor (সুপারভাইজার) within 3 seconds.
And third, the supervisor checks the temperature (টেম্পারেচার) history (হিস্ট্রি) chart, sees exactly (এক্স্যাক্টলি) when the heat started drifting (ড্রিফটিং), and adjusts (অ্যাডজাস্টস) the machine right away.

▶ The Result (রেজাল্ট):
That instant (ইনস্ট্যান্ট) warning saves entire (এনটায়ার) fabric lots from burning and cuts down unplanned downtime (আনপ্ল্যানড ডাউনটাইম) significantly (সিগনিফিক্যান্টলি)."

--------------------------------------------------------------------------------
SLIDE 09: TEXTILE OS & DIGITAL TWIN CORE (ভিন্ন ভিন্ন মেশিনকে এক ডিজিটাল টুইনে আনা)
[পিলার: Digital Twin Architecture — Core Focus]
================================================================================
স্লাইডের উদ্দেশ্য:
ইন্ডাস্ট্রি ভিজিটে দেখা বিভিন্ন ব্র্যান্ড ও পুরোনো মেশিনকে একত্র করে কীভাবে একটি ইউনিফাইড Digital Twin তৈরি করা হয়েছে তা বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"This slide covers the core Digital Twin (ডিজিটাল টুইন) layer (লেয়ার) we built — called Textile OS (টেক্সটাইল ও-এস).

▶ What We Found During the Factory Visit:
When we visited the client's industry (ইন্ডাস্ট্রি), we quickly noticed (নোটিসড) that the machines (মেশিনস) didn't speak one common language (ল্যাঙ্গুয়েজ). They had modern (মডার্ন) German Monforts (মনফোর্টস) stenters (স্টেন্টার), Italian (ইতালিয়ান) machines, and even 30-year-old controllers (কন্ট্রোলার). Some used Modbus (মডবাস), some used Siemens S7 (সিমেন্স এস-সেভেন), and others used OPC-UA (ও-পি-সি ইউ-এ) or RS-485 (আর-এস ফোর-এইটি-ফাইভ). Still, the client wanted every single machine inside one Digital Twin (ডিজিটাল টুইন).

▶ Our Solution (সলিউশন):
So we engineered (ইঞ্জিনিয়ার্ড) Textile OS as a universal (ইউনিভার্সাল) normalization (নরমালাইজেশন) layer.
Our Edge Gateways (এজ গেটওয়ে) read each machine in its native (নেটিভ) protocol (প্রোটোকল) — temperature (টেম্পারেচার), humidity (হিউমিডিটি), steam pressure (স্টিম প্রেশার), speed, and 3-phase power.
Right at the edge, we normalize (নরমালাইজ) all those signals (সিগন্যালস) into one clean, standard (স্ট্যান্ডার্ড) JSON schema (জে-সন স্কিমা).
That clean stream (স্ট্রিম) continuously (কন্টিনিউয়াসলি) updates a live virtual (ভার্চুয়াল) model (মডেল) — a true Digital Twin (ডিজিটাল টুইন) — for every machine in the backend (ব্যাকএন্ড).

▶ The Result (রেজাল্ট):
Whether a machine is brand new or 30 years old, inside AutoTaskX (অটো-টাস্ক-এক্স) every machine behaves (বিহেভস) like one standardized (স্ট্যান্ডার্ডাইজড) Digital Twin node (নোড)."

--------------------------------------------------------------------------------
SLIDE 10: IOT DATA TRACE UNDER 25MS (একটি সেন্সর রিডিংয়ের ২৫ মিলিসেকেন্ডের যাত্রা)
[পিলার: Data Pipeline Latency & Performance]
================================================================================
স্লাইডের উদ্দেশ্য:
একটি সিঙ্গেল রিডিংয়ের <25ms এন্ড-টু-এন্ড যাত্রা সহজভাবে ধাপে ধাপে দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Since the client asked for true real-time (রিয়েল-টাইম) visibility (ভিজিবিলিটি), keeping latency (লেইটেন্সি) ultra-low (আল্ট্রা-লো) was a top priority (প্রায়োরিটি) in our data pipeline (ডাটা পাইপলাইন). Let's trace (ট্রেস) just one single temperature (টেম্পারেচার) reading (রিডিং) from start to finish:

First, inside Stenter (স্টেন্টার) zone four, a PT100 (পি-টি হান্ড্রেড) sensor (সেন্সর) reads 185.5 degrees Celsius (সেলসিয়াস) every 100 milliseconds (মিলিসেকেন্ড).
Next, the IoT Gateway (আই-ও-টি গেটওয়ে) converts (কনভার্টস) that analog (অ্যানালগ) signal into a tiny MQTT (এম-কিউ-টি-টি) packet (প্যাকেট).
It travels across the factory local network (লোকাল নেটওয়ার্ক) to our FastAPI (ফাস্ট-এ-পি-আই) backend (ব্যাকএন্ড).
AutoTaskX checks the safety threshold (সেফটি থ্রেশহোল্ড), updates the Digital Twin (ডিজিটাল টুইন), writes it to TimescaleDB (টাইম-স্কেল-ডি-বি), and pushes it to the manager's live screen.

In fact, if we click 'Animate Data Flow (অ্যানিমেট ডাটা ফ্লো)' right here, you can see all six hops happen in under 25 milliseconds (মিলিসেকেন্ড). On the dashboard (ড্যাশবোর্ড), it feels completely (কমপ্লিটলি) instant (ইনস্ট্যান্ট)."

--------------------------------------------------------------------------------
SLIDE 11: WHY MQTT? DATA TRANSPORT DECISION (এম-কিউ-টি-টি কেন ব্যবহার করলাম?)
[পিলার: MQTT Architecture & Protocol Choice]
================================================================================
স্লাইডের উদ্দেশ্য:
সেন্সরের জন্য HTTP-র বদলে MQTT এবং ছবির জন্য HTTPS S3 বেছে নেওয়ার পরিষ্কার যুক্তি দেওয়া।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Now, when designing (ডিজাইনিং) the architecture (আর্কিটেকচার) blueprint (ব্লুপ্রিন্ট), a key decision (ডিসিশন) was picking MQTT (এম-কিউ-টি-টি) instead (ইনস্টেড) of regular (রেগুলার) HTTP REST APIs (এইচ-টি-টি-পি রেস্ট এ-পি-আই) for machine telemetry (টেলেমেট্রি).

▶ The Problem:
Imagine (ইমাজিন) 50 machines sending sensor (সেন্সর) readings every second over standard HTTP (এইচ-টি-টি-পি). HTTP carries heavy headers (হেডার) and constant (কনস্ট্যান্ট) connection (কানেকশন) overhead (ওভারহেড). On a noisy (নয়েজি) factory Wi-Fi (ওয়াই-ফাই) network, that slows things down and drops packets (প্যাকেট).

▶ Our Solution (সলিউশন):
So we enforced (এনফোর্সড) two strict (স্ট্রিক্ট) rules in our design:
Rule one: Small sensor telemetry (টেলেমেট্রি) goes through our EMQX MQTT Broker (ই-এম-কিউ-এক্স এম-কিউ-টি-টি ব্রোকার). Since temperature (টেম্পারেচার) or RPM (আর-পি-এম) is only a few bytes, MQTT's tiny 2-byte header (হেডার) and Pub/Sub (পাব/সাব) model stream (স্ট্রিম) data reliably (রিলায়েবলি) into our Digital Twin (ডিজিটাল টুইন) without losing readings.
Rule two: Large 20-megabyte (মেগাবাইট) images NEVER touch MQTT. They go directly (ডিরেক্টলি) over HTTPS (এইচ-টি-টি-পি-এস) to AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) so the broker (ব্রোকার) never gets blocked.

▶ The Result (রেজাল্ট):
The client gets fast, lightweight (লাইটওয়েট), rock-solid (রক-সলিড) communication (কমিউনিকেশন) across the entire (এনটায়ার) factory."

--------------------------------------------------------------------------------
SLIDE 12: STORAGE ARCHITECTURE (তিনটি বিশেষায়িত ডেটাবেজ কেন?)
[পিলার: Data Engineering & Polyglot Storage]
================================================================================
স্লাইডের উদ্দেশ্য:
ডেটার ধরন অনুযায়ী ৩টি আলাদা স্টোরেজ ব্যবহার করার কারণ সহজভাবে ব্যাখ্যা করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"From a Data Engineering (ডাটা ইঞ্জিনিয়ারিং) standpoint (স্ট্যান্ডপয়েন্ট), putting every type of data into one single database (ডাটাবেজ) doesn't scale well. So in our blueprint (ব্লুপ্রিন্ট), we chose three specialized (স্পেশালাইজড) storage (স্টোরেজ) systems, each doing one job well:

First, PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) for relational (রিলেশনাল) business data — things like buyer orders, user roles, machine profiles (প্রোফাইলস), and dye recipes (রেসিপিস) that require (রিকয়ার) strict (স্ট্রিক্ট) ACID (অ্যাসিড) accuracy (অ্যাকিউরেসি).

Second, TimescaleDB (টাইম-স্কেল-ডি-বি) for time-series (টাইম-সিরিজ) sensor (সেন্সর) data. Because we collect millions (মিলিয়নস) of timestamped (টাইমস্ট্যাম্পড) readings, a regular (রেগুলার) table gets very slow over time. TimescaleDB runs on top of PostgreSQL using Hypertables (হাইপার-টেবলস) — it automatically (অটোমেটিক্যালি) chunks data by time and gives us up to 95 percent (পারসেন্ট) compression (কম্প্রেশন).

And third, AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) for heavy files — like high-resolution (হাই-রেজোলিউশন) fabric (ফ্যাব্রিক) defect (ডিফেক্ট) scans and PDF reports (রিপোর্টস).

So whenever the client's managers (ম্যানেজারস) open a batch history (হিস্ট্রি), all three work smoothly (স্মুথলি) together without slowing each other down."

--------------------------------------------------------------------------------
SLIDE 13: REAL-TIME DELIVERY PIPELINE (লাইভ আপডেট বনাম হিস্টোরিক্যাল রিপোর্ট)
[পিলার: Data Serving & User Experience]
================================================================================
স্লাইডের উদ্দেশ্য:
অপারেটরের লাইভ স্ক্রিন আর ম্যানেজমেন্টের ভারী রিপোর্টের মধ্যে সার্ভার লোড কীভাবে আলাদা করা হয়েছে তা দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Once the data is stored, serving (সার্ভিং) it efficiently (এফিশিয়েন্টলি) to two very different user groups was another requirement (রিকোয়ারমেন্ট) we captured (ক্যাপচার্ড) early on.

▶ The Problem:
Floor operators (অপারেটর) need zero-lag live updates (আপডেটস) — they shouldn't have to refresh (রিফ্রেশ) their screen. Meanwhile (মিনহোয়াইল), the client's plant directors (ডিরেক্টর) run heavy historical (হিস্টোরিক্যাল) charts across weeks of shift data. If both shared one pathway (পাথওয়ে), a heavy report could freeze the live monitor (মনিটর).

▶ Our Solution (সলিউশন):
So we split data delivery (ডেলিভারি) into two dedicated (ডেডিকেটেড) lanes:
For live monitoring (মনিটরিং), FastAPI WebSockets (ফাস্ট-এ-পি-আই ওয়েব-সকেট) push Digital Twin (ডিজিটাল টুইন) state changes straight to the Next.js (নেক্সট-জে-এস) dashboard (ড্যাশবোর্ড) without polling (পোলিং).
For historical (হিস্টোরিক্যাল) trends and shift analytics (অ্যানালিটিক্স), we serve cached REST APIs (ক্যাশড রেস্ট এ-পি-আই) backed by TimescaleDB aggregates (অ্যাগ্রিগেটস).

▶ The Result (রেজাল্ট):
Even when a director (ডিরেক্টর) loads a 30-day energy (এনার্জি) report, the floor operator's (অপারেটরস) live machine monitor (মনিটর) stays completely (কমপ্লিটলি) smooth with zero lag."

--------------------------------------------------------------------------------
SLIDE 14: FEATURE 05 — ERP INTEGRATION (ফ্যাক্টরি থেকে অফিসের ই-আর-পি অটোমেশন)
[পিলার: Enterprise Data Integration]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের চাহিদা অনুযায়ী শপফ্লোরের সাথে হেড অফিসের ERP (SAP, Datatex, Infor)-এর স্বয়ংক্রিয় সংযোগ দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Feature (ফিচার) five addresses (অ্যাড্রেসেস) something the client specifically (স্পেসিফিক্যালি) asked for during our office meetings — connecting (কানেক্টিং) the factory floor directly (ডিরেক্টলি) with their head-office business software (সফটওয়্যার).

▶ The Problem:
Like most large textile groups, the client already runs an ERP (ই-আর-পি) such as SAP (এস-এ-পি), Datatex NOW (ডাটাটেক্স নাউ), or Infor M3 (ইনফর এম-থ্রি). But previously (প্রিভিয়াসলি), operators (অপারেটরস) wrote production (প্রোডাকশন) logs on paper, and office staff typed them into the ERP one or two days later — often with mistakes.

▶ Our Solution (সলিউশন):
So we built a two-way ERP bridge:
Work orders come down automatically (অটোমেটিক্যালি) from the ERP into AutoTaskX (অটো-টাস্ক-এক্স) as digital (ডিজিটাল) jobs.
And once a dyeing (ডাইং) or inspection (ইন্সপেকশন) batch finishes, actual (অ্যাকচুয়াল) meters produced and exact (এক্স্যাক্ট) chemical (কেমিক্যাল) amounts consumed (কনজিউমড) sync (সিঙ্ক) straight back up into the ERP inventory (ইনভেন্টরি).

▶ The Result (রেজাল্ট):
No more two-day reporting (রিপোর্টিং) delays, no manual (ম্যানুয়াল) data entry errors, and 100 percent (পারসেন্ট) transparent (ট্রান্সপারেন্ট) inventory (ইনভেন্টরি) tracking (ট্র্যাকিং) for the client."

--------------------------------------------------------------------------------
SLIDE 15: COMPLETE 4-ZONE ARCHITECTURE (পুরো সিস্টেমের ৪-জোন ব্লুপ্রিন্ট)
[পিলার: System Architecture & Scalability]
================================================================================
স্লাইডের উদ্দেশ্য:
৪টি জোনে পুরো আর্কিটেকচার ব্লুপ্রিন্টের স্কেলেবিলিটি ও ক্লিন ডিজাইন তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"This slide shows the complete (কমপ্লিট) software (সফটওয়্যার) architecture (আর্কিটেকচার) blueprint (ব্লুপ্রিন্ট) we delivered (ডেলিভার্ড), organized (অর্গানাইজড) into four clean zones:

Zone one is the Physical Factory (ফিজিক্যাল ফ্যাক্টরি) — stenters (স্টেন্টার), dyeing (ডাইং) machines, looms (লুমস), cameras, and over 100 sensors (সেন্সর).
Zone two is the Connection Layer (কানেকশন লেয়ার) — Edge Gateways (এজ গেটওয়ে) reading Modbus (মডবাস) or OPC-UA (ও-পি-সি ইউ-এ), connected to our central EMQX MQTT Broker (ই-এম-কিউ-এক্স এম-কিউ-টি-টি ব্রোকার).
Zone three is the Core & Storage Layer — our FastAPI (ফাস্ট-এ-পি-আই) backend (ব্যাকএন্ড), AI vision (ভিশন) models, Digital Twin (ডিজিটাল টুইন) state, and our three databases (ডাটাবেজেস): PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল), TimescaleDB (টাইম-স্কেল-ডি-বি), and AWS S3 (এ-ডব্লিউ-এস এস-থ্রি).
Zone four is Delivery & Enterprise (এন্টারপ্রাইজ) — the Next.js (নেক্সট-জে-এস) dashboard (ড্যাশবোর্ড), mobile QA app, SMS alerts, and the ERP bridge.

And you know, when we planned (প্ল্যান্ড) this blueprint (ব্লুপ্রিন্ট), the client wanted to make sure they could expand (এক্সপ্যান্ড) later. Because the design is loosely coupled (লুজলি কাপল্ড), if they add 50 more machines in another building tomorrow, we just plug in new gateways (গেটওয়েজ) in Zones one and two — zero core code changes needed."

--------------------------------------------------------------------------------
SLIDE 16: MEASURABLE BUSINESS OUTCOMES (গাজীপুর মিলে বাস্তব ফলাফল ও আরওআই)
[পিলার: Outcomes & Business ROI]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের গাজীপুর মিলে ৪ মাসে পাওয়া বাস্তব ও পরিমাপযোগ্য ফলাফলগুলো তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"At the end of the day, any automation (অটোমেশন) and Digital Twin (ডিজিটাল টুইন) project has to prove itself with real business results. On this slide, you're looking at a live snapshot (স্ন্যাপশট) from the client's Gazipur (গাজীপুর) Textile Mill number four:

Out of 26 connected machines, 24 are running non-stop right now, and 2 are offline for scheduled (স্কেজুয়ালড) maintenance (মেইনটেন্যান্স) — so nothing on the floor is a surprise (সারপ্রাইজ) anymore.
Stenter (স্টেন্টার) temperature (টেম্পারেচার) is holding steady (স্টেডি) at 185.5 degrees with zero critical (ক্রিটিক্যাল) alerts.
In a single day, we tracked 42,500 meters of fabric (ফ্যাব্রিক) in real time.
With AI vision inspection (ইন্সপেকশন), the Right-First-Time (রাইট-ফার্স্ট-টাইম) quality pass rate reached 99.2 percent (পারসেন্ট).
And overall (ওভারঅল) equipment (ইকুইপমেন্ট) effectiveness (ইফেক্টিভনেস) — or OEE (ও-ই-ই) — improved (ইমপ্রুভড) by 14 percent within just four months.

Now the client can literally (লিটারালি) open a tablet (ট্যাবলেট) from anywhere in the world and see how their entire (এনটায়ার) plant is performing (পারফর্মিং)."

--------------------------------------------------------------------------------
SLIDE 17: AI AUTOMATION & FUTURE ROADMAP (এ-আই অটোমেশন ও ভবিষ্যৎ পরিকল্পনা)
[পিলার: AI Automation & Future Scalability]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের পরবর্তী ধাপের AI Automation ও Predictive Maintenance রোডম্যাপ তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Because the first four months delivered (ডেলিভার্ড) strong results, we also mapped out a five-stage future roadmap (রোডম্যাপ) with the client to take AI automation (এ-আই অটোমেশন) even further:

Stage one is Connect More — expanding (এক্সপ্যান্ডিং) IoT gateways (গেটওয়েজ) across spinning (স্পিনিং), weaving (উইভিং), and knitting (নিটিং) sheds for 100 percent floor visibility (ভিজিবিলিটি).
Stage two is Automated (অটোমেটেড) Inspection (ইন্সপেকশন) — adding automatic (অটোমেটিক) camera triggers (ট্রিগারস) on unrolling (আনরোলিং) frames so every meter is scanned hands-free.
Stage three is Historical (হিস্টোরিক্যাল) AI Analytics (অ্যানালিটিক্স) — using months of TimescaleDB (টাইম-স্কেল-ডি-বি) data to predict (প্রিডিক্ট) seasonal (সিজনাল) dye behavior (বিহেভিয়ার).
Stage four is Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স) — analyzing (অ্যানালাইজিং) motor vibration (ভাইব্রেশন) and bearing (বেয়ারিং) heat patterns (প্যাটার্নস) so AI warns engineers (ইঞ্জিনিয়ার্স) before a machine breaks down.
And stage five is Closed-Loop Control (ক্লোজড-লুপ কন্ট্রোল) — where the Digital Twin (ডিজিটাল টুইন) can safely send automated (অটোমেটেড) adjustments (অ্যাডজাস্টমেন্টস) back to the PLC (পি-এল-সি) to fine-tune (ফাইন-টিউন) machine speed or heat automatically (অটোমেটিক্যালি)."

--------------------------------------------------------------------------------
SLIDE 18: CONCLUSION & Q&A (সমাপ্তি ও প্রশ্নোত্তর পর্ব)
[পিলার: Closing Statement]
================================================================================
স্লাইডের উদ্দেশ্য:
কোনো ব্যক্তিগত পরিচয় রিপিট না করে ক্লায়েন্ট প্রজেক্টের পুরো যাত্রা ও ৩ জনের টিমে আপনার ৪০-৫০% অবদান সংক্ষেপে শেষ করা এবং টেকনিক্যাল প্রশ্নের জন্য আমন্ত্রণ জানানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"To wrap up, AutoTaskX (অটো-টাস্ক-এক্স) isn't a classroom concept (কনসেপ্ট) or a mockup (মক-আপ). It started when a prominent (প্রমিনেন্ট) Bangladeshi textile client came to our office asking for complete (কমপ্লিট) automation (অটোমেশন) and a live Digital Twin (ডিজিটাল টুইন). From visiting their industry (ইন্ডাস্ট্রি) and organizing (অর্গানাইজিং) the requirements (রিকোয়ারমেন্টস) to creating (ক্রিয়েটিং) the software (সফটওয়্যার) blueprint (ব্লুপ্রিন্ট), our three-developer (থ্রি-ডেভেলপার) core team built both the backend (ব্যাকএন্ড) and frontend (ফ্রন্টএন্ড) in four months — and as one of the main backend engineers (ইঞ্জিনিয়ার্স) contributing (কন্ট্রিবিউটিং) roughly (রাফলি) 40 to 50 percent (পারসেন্ট) of the overall (ওভারঅল) build, it's great to see the platform (প্ল্যাটফর্ম) running 24/7 in live production (প্রোডাকশন) today.

By combining (কম্বাইনিং) clean Data Engineering (ডাটা ইঞ্জিনিয়ারিং), reliable (রিলায়েবল) MQTT (এম-কিউ-টি-টি) streaming (স্ট্রিমিং), Digital Twin synchronization (সিঙ্ক্রোনাইজেশন), and practical (প্র্যাকটিক্যাল) AI automation (এ-আই অটোমেশন), we turned disconnected (ডিসকানেক্টেড) machines into one unified (ইউনিফাইড) smart factory.

Thank you so much for your attention (অ্যাটেনশন). I'd love to answer any technical (টেকনিক্যাল) questions you have about our backend architecture (আর্কিটেকচার), Digital Twin setup, MQTT pipeline (পাইপলাইন), or AI workflow (ওয়ার্কফ্লো)."

================================================================================
MASTER CHEAT SHEET: ৬টি গুরুত্বপূর্ণ ইন্টারভিউ প্রশ্ন ও সাবলীল ইংরেজি উত্তর
================================================================================

প্রশ্ন ১: "How do you keep the Digital Twin (ডিজিটাল টুইন) always synchronized (সিঙ্ক্রোনাইজড) with the physical (ফিজিক্যাল) machines?"
স্মার্ট উত্তর:
"You know, every physical (ফিজিক্যাল) machine has an Edge Gateway (এজ গেটওয়ে) polling (পোলিং) sensors (সেন্সর) every 100 milliseconds (মিলিসেকেন্ড). It normalizes (নরমালাইজেস) the reading into standard (স্ট্যান্ডার্ড) JSON (জে-সন) and publishes (পাবলিশেস) it over MQTT (এম-কিউ-টি-টি) to our EMQX Broker (ই-এম-কিউ-এক্স ব্রোকার). Our FastAPI (ফাস্ট-এ-পি-আই) backend (ব্যাকএন্ড) receives (রিসিভস) that stream (স্ট্রিম) immediately (ইমিডিয়েটলি), updates the Digital Twin state in memory (মেমোরি), saves history (হিস্ট্রি) to TimescaleDB (টাইম-স্কেল-ডি-বি), and pushes live updates over WebSockets (ওয়েব-সকেট) — all in under 25 milliseconds (মিলিসেকেন্ড)."

প্রশ্ন ২: "Why did you choose MQTT (এম-কিউ-টি-টি) instead (ইনস্টেড) of regular (রেগুলার) HTTP REST APIs (এইচ-টি-টি-পি রেস্ট এ-পি-আই) for sensor (সেন্সর) data?"
স্মার্ট উত্তর:
"To be honest (টু বি অনেস্ট), HTTP (এইচ-টি-টি-পি) is great for normal web requests (রিকোয়েস্টস), but for high-frequency (হাই-ফ্রিকোয়েন্সি) sensor (সেন্সর) data, opening and closing HTTP connections (কানেকশনস) with large headers (হেডার) wastes a lot of bandwidth (ব্যান্ডউইথ). MQTT (এম-কিউ-টি-টি) only uses a tiny 2-byte header on one persistent (পারসিস্টেন্ট) connection (কানেকশন). Plus, with QoS Level 1 (কিউ-ও-এস লেভেল ওয়ান), even if the factory Wi-Fi flickers (ফ্লিকারস), we don't lose critical (ক্রিটিক্যাল) machine readings (রিডিংস)."

প্রশ্ন ৩: "Why TimescaleDB (টাইম-স্কেল-ডি-বি)? Why not just plain PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) or MongoDB (মঙ্গো-ডি-বি)?"
স্মার্ট উত্তর:
"Actually (অ্যাকচুয়ালি), we needed both worlds for the client. Their orders and dye recipes (রেসিপিস) are strictly (স্ট্রিক্টলি) relational (রিলেশনাল), so PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) gives us solid ACID (অ্যাসিড) reliability (রিলায়াবিলিটি). But storing millions (মিলিয়নস) of sensor rows in a plain table slows queries (কুয়েরিস) down over time. Since TimescaleDB (টাইম-স্কেল-ডি-বি) runs right inside PostgreSQL using Hypertables (হাইপার-টেবলস), we get automatic (অটোমেটিক) time partitioning (পার্টিশনিং) and 95 percent (পারসেন্ট) storage compression (কম্প্রেশন) without managing (ম্যানেজিং) two separate (সেপারেট) database (ডাটাবেজ) engines (ইঞ্জিনস)."

প্রশ্ন ৪: "What happens if the factory internet drops while uploading (আপলোডিং) a 20MB inspection (ইন্সপেকশন) image?"
স্মার্ট উত্তর:
"That's a very real factory challenge (চ্যালেঞ্জ) we saw during our mill visit, so we planned for it right away. On the Edge PC (এজ পি-সি), we implemented (ইমপ্লিমেন্টেড) a local FIFO disk buffer (ফিফো ডিস্ক বাফার) and queue (কিউ). Every image is written to local storage (স্টোরেজ) first, and it is never deleted (ডিলিটেড) until AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) confirms (কনফার্মস) a successful (সাকসেসফুল) 200 OK upload (আপলোড). As soon as the internet comes back, pending (পেন্ডিং) images sync (সিঙ্ক) automatically (অটোমেটিক্যালি) in exact (এক্স্যাক্ট) order — zero lost frames (ফ্রেমস)."

প্রশ্ন ৫: "Why did you pick FastAPI (ফাস্ট-এ-পি-আই) over Django (জ্যাঙ্গো) for the backend (ব্যাকএন্ড)?"
স্মার্ট উত্তর:
"Basically (বেসিক্যালি), we had hundreds (হান্ড্রেডস) of concurrent (কনকারেন্ট) IoT streams (স্ট্রিমস) and live WebSocket (ওয়েব-সকেট) dashboards (ড্যাশবোর্ডস) running at the same time. Traditional (ট্র্যাডিশনাল) Django (জ্যাঙ্গো) is mostly synchronous (সিঙ্ক্রোনাস) and heavier for high-concurrency (হাই-কনকারেন্সি) streaming (স্ট্রিমিং). FastAPI (ফাস্ট-এ-পি-আই) is built on native (নেটিভ) AsyncIO (অ্যাসিঙ্ক-আই-ও) and ASGI (এ-এস-জি-আই), so it handles many simultaneous (সাইমালটেনিয়াস) MQTT and WebSocket connections (কানেকশনস) smoothly using much less CPU (সি-পি-ইউ) and RAM (র‍্যাম)."

প্রশ্ন ৬: "How is AI automation (এ-আই অটোমেশন) delivering (ডেলিভারিং) real value (ভ্যালু) here instead (ইনস্টেড) of just being a buzzword (বাজওয়ার্ড)?"
স্মার্ট উত্তর:
"To be honest (টু বি অনেস্ট), the client didn't want AI just for show — they wanted real ROI (আর-ও-আই). So we used it in three practical (প্র্যাকটিক্যাল) places: first, OpenCV (ওপেন-সি-ভি) and YOLO (ইয়োলো) catching sub-millimeter (সাব-মিলিমিটার) fabric defects (ডিফেক্টস) at up to 120 meters per minute; second, automated (অটোমেটেড) thermal (থার্মাল) anomaly (অ্যানোমালি) alerts that prevented (প্রিভেন্টেড) burning fabric at 192 degrees; and third, building clean historical (হিস্টোরিক্যাল) data in TimescaleDB (টাইম-স্কেল-ডি-বি) so we can run Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স) on motor vibrations (ভাইব্রেশনস) before breakdowns (ব্রেকডাউনস) happen."

================================================================================
[End of Guide — Read calmly, smile, and speak clearly. Best of luck!]
================================================================================
"""

with open('AutoTaskX_Presentation_Guide_Bangla.txt', 'w', encoding='utf-8') as f:
    f.write(guide_text)

print("Generated AutoTaskX_Presentation_Guide_Bangla.txt successfully.")

slides = []
blocks = re.split(r'SLIDE (\d+): ([^\n]+)', guide_text)

pillar_map = {
    "01": "1. Client Vision & Overview",
    "02": "1. Client Pain Points & Visit",
    "03": "2. Architecture Blueprint",
    "04": "2. Data Pipeline & MQTT",
    "05": "3. Client Lab Automation",
    "06": "3. AI Vision Automation",
    "07": "4. Challenge & Data Offload",
    "08": "4. AI Anomaly & Safety",
    "09": "2. Digital Twin Core",
    "10": "2. Data Trace (<25ms)",
    "11": "5. MQTT Protocol Decision",
    "12": "5. Polyglot Data Storage",
    "13": "2. Real-time Data Serving",
    "14": "3. Enterprise ERP Bridge",
    "15": "2. 4-Zone Scalable Blueprint",
    "16": "6. Client ROI & Impact",
    "17": "2. AI & Autonomous Roadmap",
    "18": "6. Summary & Panel Q/A"
}

engineering_knowledge = {
    "01": [
        {"label": "Client Profile", "val": "Prominent Bangladeshi Textile Industry Leader"},
        {"label": "Team & Role", "val": "3-Developer Core Team · Main Backend Engineer (~40–50%)"},
        {"label": "Discovery Workflow", "val": "Office Consultation → Industry Visit → Blueprint"},
        {"label": "Production Proof", "val": "4-Month Build · Running 24/7 Live (<25ms HUD)"}
    ],
    "02": [
        {"label": "Client Pain Points", "val": "Manual Pen-Paper Logs & Disconnected Mill Islands"},
        {"label": "Factory Visit Audit", "val": "Verified Legacy Machinery & Shift-End Blindspots"},
        {"label": "Business Risk", "val": "Up to 10,000m Fabric Batch Rejection Losses"},
        {"label": "Target Outcome", "val": "Automated Data-Driven Digital Twin Visibility"}
    ],
    "03": [
        {"label": "Solution Blueprint", "val": "5 Modular Engines Sharing One Unified Data Pipeline"},
        {"label": "No Hardware Swap", "val": "Built Around Existing Dyeing, Stenter & Lab Assets"},
        {"label": "Integration Model", "val": "Event-Driven MQTT Pub/Sub via EMQX Broker"},
        {"label": "AI Automation", "val": "Automated Dye Math, Defect Detection & Anomaly Alerts"}
    ],
    "04": [
        {"label": "Tier 1 (Sense)", "val": "PT100 RTD Sensors & Basler CoaXPress 16K Cameras"},
        {"label": "Tier 2 (Connect)", "val": "Edge Gateway -> Normalized JSON -> EMQX MQTT Broker"},
        {"label": "Tier 3 (Process)", "val": "FastAPI Async Engine -> Digital Twin State + TimescaleDB"},
        {"label": "Tier 4 (Deliver)", "val": "WebSocket Live Push to Next.js UI (<25ms E2E)"}
    ],
    "05": [
        {"label": "Client Lab Need", "val": "Eliminate 5-6 Hour Manual Lab Dye Trial-and-Error"},
        {"label": "Solution Engine", "val": "Kubelka-Munk Spectral Math + Automated Recipe Calc"},
        {"label": "Quality Precision", "val": "CIE ΔE < 1.0 (85%+ First-Pass Match, Lab Validated)"},
        {"label": "Dispensary Sync", "val": "Exact Grams per 100kg Sent to Auto-Dispenser"}
    ],
    "06": [
        {"label": "Client QA Need", "val": "Catch <0.5mm Flaws at 80-120 m/min Automatically"},
        {"label": "Hardware Inputs", "val": "Basler racer 2L (16K Line-Scan) + Floor Mobile App"},
        {"label": "AI Automation", "val": "OpenCV Image Stitching + YOLO Defect Classification"},
        {"label": "Audit Trail", "val": "Instant Bounding Box & Automated Roll Defect Report"}
    ],
    "07": [
        {"label": "Key Challenge", "val": "20MB Uncompressed TIFF Frames Crashing API / MQTT"},
        {"label": "Blueprint Solution", "val": "Parallel Pre-signed AWS S3 Direct Upload from Edge PC"},
        {"label": "MQTT Separation", "val": "Only Lightweight Scan Metadata & Alerts Sent via MQTT"},
        {"label": "Stability Result", "val": "0% API Memory Bottleneck Under Peak Line Speed"}
    ],
    "08": [
        {"label": "Real Scenario", "val": "Stenter Chamber Heat Spiked to 192°C (Limit 185°C)"},
        {"label": "AI & Twin Action", "val": "Instant Red Dashboard Alert + SMS Within 3 Seconds"},
        {"label": "Root Diagnosis", "val": "Supervisor Traced Exact Drift Start on History Chart"},
        {"label": "Business Value", "val": "Prevented Fabric Burning & Reduced Unplanned Downtime"}
    ],
    "09": [
        {"label": "Visit Finding", "val": "Mixed Fleet: Modern European Stenters + 30-Year PLCs"},
        {"label": "Supported Protocols", "val": "Modbus RTU/TCP, Siemens S7, OPC-UA, RS-485 Serial"},
        {"label": "Digital Twin Layer", "val": "Textile OS Edge Normalization to Standard JSON Schema"},
        {"label": "Virtual Sync", "val": "Every Machine Unified as One Digital Twin Node"}
    ],
    "10": [
        {"label": "Sensor Trace", "val": "PT100 RTD (185.5°C @ 100ms) -> Gateway -> MQTT -> UI"},
        {"label": "Packet Overhead", "val": "Lightweight 2-Byte MQTT Header (QoS 1)"},
        {"label": "Pipeline Latency", "val": "Sub-25ms End-to-End Hardware to Live Screen"},
        {"label": "Interactive Demo", "val": "Click 'Animate Data Flow' on Slide 10 to Trace Live"}
    ],
    "11": [
        {"label": "Protocol Split", "val": "MQTT for Tiny Sensor Telemetry vs HTTPS S3 for Blobs"},
        {"label": "Why EMQX MQTT", "val": "Persistent Connection, Low Bandwidth, Zero Drop QoS"},
        {"label": "Why Direct S3", "val": "Keeps 20MB Vision Blobs Out of MQTT Broker Memory"},
        {"label": "Digital Twin Feed", "val": "High-Frequency Pub/Sub Streams Update Twin State Live"}
    ],
    "12": [
        {"label": "Storage Strategy", "val": "Polyglot Persistence Matched to Data Workload"},
        {"label": "PostgreSQL", "val": "ACID Relational Orders, Users, Dye Recipes & Batches"},
        {"label": "TimescaleDB", "val": "Hypertables with Auto-Chunking & 95% Compression"},
        {"label": "AWS S3", "val": "20MB TIFF Fabric Scans & Generated PDF Reports"}
    ],
    "13": [
        {"label": "Dual Channels", "val": "WebSockets (Live Floor) + Cached REST APIs (Reports)"},
        {"label": "Floor Operators", "val": "Zero-Polling Live Digital Twin Screen (<25ms)"},
        {"label": "Management", "val": "Heavy 30-Day Trends & Shift Energy Analytics"},
        {"label": "Performance", "val": "Analytical Queries Never Freeze Real-Time Monitoring"}
    ],
    "14": [
        {"label": "Client ERP Need", "val": "Eliminate 24-48 Hour Manual Delay to SAP / Datatex"},
        {"label": "Work Orders Down", "val": "ERP Orders Auto-Push as Digital Shopfloor Jobs"},
        {"label": "Output Sync Up", "val": "Actual Meters & Chemical Usage Auto-Deduct in ERP"},
        {"label": "Audit Impact", "val": "100% Paperless & Tamper-Proof Production Ledgers"}
    ],
    "15": [
        {"label": "Zone 1 & Zone 2", "val": "100+ Floor Sensors -> Edge Gateways -> EMQX MQTT"},
        {"label": "Zone 3 (Core)", "val": "FastAPI, AI Models, Digital Twin & Polyglot Storage"},
        {"label": "Zone 4 (Apps)", "val": "Next.js Dashboard, Mobile QA, SMS & ERP Connector"},
        {"label": "Client Expansion", "val": "Loosely Coupled — Add 50 Machines Without Code Rewrites"}
    ],
    "16": [
        {"label": "Client Deployment", "val": "Gazipur Textile Mill #04 — 26 Connected Machines"},
        {"label": "Fleet Status", "val": "24 Running Live · 2 Planned Maintenance · 0 Alerts"},
        {"label": "Daily Throughput", "val": "42,500m Tracked Live · 99.2% Vision Pass Rate (RFT)"},
        {"label": "Client ROI", "val": "+14% OEE Improvement Achieved Within 4 Months"}
    ],
    "17": [
        {"label": "Phase 1 & 2", "val": "100% Mill Expansion + Automated Inline Trigger Rigs"},
        {"label": "Phase 3 (Analytics)", "val": "TimescaleDB Historical AI Modeling for Seasonal Shades"},
        {"label": "Phase 4 (AI PdM)", "val": "Vibration & Bearing Heat AI Predictive Maintenance"},
        {"label": "Phase 5 (Autonomy)", "val": "Closed-Loop Digital Twin Feedback to Adjust PLC Speed"}
    ],
    "18": [
        {"label": "Engagement Arc", "val": "Office Consultation → Factory Visit → Blueprint → Live"},
        {"label": "Team Contribution", "val": "3-Developer Core Team · Main Backend (~40–50%)"},
        {"label": "Core Pillars", "val": "Digital Twin · EMQX MQTT · Polyglot Data · AI Vision"},
        {"label": "Q&A Readiness", "val": "Ready for Architecture, Pipeline & Data Deep Dive"}
    ]
}

cheat_marker = 'MASTER CHEAT SHEET: ৬টি গুরুত্বপূর্ণ ইন্টারভিউ প্রশ্ন ও সাবলীল ইংরেজি উত্তর'
cheat_parts = guide_text.split(cheat_marker)
cheat_text = cheat_parts[1] if len(cheat_parts) > 1 else ''
cheat_questions = []
if cheat_text:
    q_matches = re.split(r'প্রশ্ন (\d+):\s*', cheat_text)
    for i in range(1, len(q_matches), 2):
        q_num = q_matches[i]
        q_content = q_matches[i+1]
        q_lines = q_content.strip().split('\n')
        q_title = q_lines[0].strip().strip('"')
        ans_part = q_content[len(q_lines[0]):].strip()
        ans_clean = re.sub(r'^স্মার্ট উত্তর:\s*', '', ans_part).strip()
        if ans_clean.startswith('"') and ans_clean.endswith('"'):
            ans_clean = ans_clean[1:-1].strip()
        ans_clean = re.split(r'={5,}', ans_clean)[0].strip()
        cheat_questions.append({
            'num': q_num,
            'title': q_title,
            'answer': ans_clean
        })

for i in range(1, len(blocks), 3):
    num = blocks[i]
    raw_title = blocks[i+1].strip()
    raw_body = blocks[i+2]

    if cheat_marker in raw_body:
        raw_body = raw_body.split(cheat_marker)[0]

    obj_match = re.search(r'স্লাইডের উদ্দেশ্য:\s*(.*?)(?=\n\s*\[|\n\s*={5,}|$)', raw_body, re.DOTALL)
    objective = obj_match.group(1).strip() if obj_match else ''

    speech_match = re.search(r'\[কীভাবে (?:শুরু করবেন|বলবেন) — স্পোকেন স্ক্রিপ্ট\]:\s*(.*?)(?=\n\s*\[|\n\s*={5,}|$)', raw_body, re.DOTALL)
    speech = speech_match.group(1).strip() if speech_match else ''

    if speech.startswith('"') and speech.endswith('"'):
        speech = speech[1:-1].strip()

    en_title = raw_title
    bn_title = ""
    if '(' in raw_title and raw_title.endswith(')'):
        idx_open = raw_title.rfind('(')
        en_title = raw_title[:idx_open].strip()
        bn_title = raw_title[idx_open + 1:-1].strip()

    slides.append({
        'num': num,
        'raw_title': raw_title,
        'en_title': en_title,
        'bn_title': bn_title,
        'pillar': pillar_map.get(num, 'Interview Topic'),
        'objective': objective,
        'speech': speech,
        'tech_points': engineering_knowledge.get(num, [])
    })

with open('guide_data.json', 'w', encoding='utf-8') as out_f:
    json.dump({'slides': slides, 'cheat_questions': cheat_questions}, out_f, ensure_ascii=False, indent=2)

print(f"Parsed {len(slides)} slides and {len(cheat_questions)} questions into guide_data.json.")
