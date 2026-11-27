import re
import json

# Complete slide-by-slide English presentation guide tailored for a Digital Twin & Data Engineer interview.
# Written in easy-to-read, natural international spoken English with Bengali pronunciations in parentheses for harder/technical words.
guide_text = """================================================================================
AUTOTASKX — ENGLISH TECHNICAL PRESENTATION & INTERVIEW MASTER GUIDE
================================================================================
Target Role: Digital Twin & Data Engineer
Candidate: Sheikh Shamiul Shakib · BUBT (CSE)
Project: AutoTaskX — Industrial IoT & Real-Time Digital Twin Platform
Delivery: Built in 4 months for a leading Bangladesh textile group · Running 24/7 Live
================================================================================

[পড়ার এবং প্রেজেন্ট করার সহজ টিপস — How to Deliver Smoothly]
--------------------------------------------------------------------------------
• পুরো স্পোকেন স্ক্রিপ্ট (Spoken Script) সহজ ও সাবলীল International English (ইন্টারন্যাশনাল ইংলিশ)-এ লেখা হয়েছে—যেন ক্লায়েন্ট বা ইন্টারভিউয়ার মনে করেন আপনি ইংলিশে খুবই ফ্লুয়েন্ট (Fluent)।
• প্রতিটি স্লাইড সাজানো হয়েছে: Problem (সমস্যা) → Solution (সমাধান) → Result (ফলাফল) ফ্লোতে।
• প্রতিটি কঠিন বা টেকনিক্যাল (Technical) ইংরেজি শব্দের ঠিক পাশেই ব্র্যাকেটে বাংলা উচ্চারণ দেওয়া আছে, যেন আপনি লেখা দেখে সাবলীলভাবে পড়তে পারেন।
• বলার সময় "You know...", "To be honest...", "Basically..." এগুলো তাড়াহুড়ো না করে একটু থেমে, আত্মবিশ্বাসের সাথে বলুন।

================================================================================
SLIDE 01: INTRODUCTION & DIGITAL TWIN VISION (পরিচিতি ও ডিজিটাল টুইন ভিশন)
[পিলার: Role & Project Objectives]
================================================================================
স্লাইডের উদ্দেশ্য:
প্রথম ৩০ সেকেন্ডে নিজের পরিচয় দেওয়া এবং আপনি যে একজন Digital Twin & Data Engineer হিসেবে কাজ করেছেন তা আত্মবিশ্বাসের সাথে তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Good morning, everyone. I'm Sheikh Shamiul Shakib, a Computer Science graduate (গ্র্যাজুয়েট) from BUBT (বি-ইউ-বি-টি). Today, I'm excited to walk you through my flagship production (প্রোডাকশন) project — AutoTaskX (অটো-টাস্ক-এক্স). Basically, it's an Industrial IoT (ইন্ডাস্ট্রিয়াল আই-ও-টি) and real-time Digital Twin (ডিজিটাল টুইন) platform built specifically (স্পেসিফিক্যালি) for textile manufacturing (ম্যানুফ্যাকচারিং).

▶ The Problem:
To be honest, when I first stepped onto the client's factory floor, they had millions of dollars worth of machinery (মেশিনারি), you know, dyeing (ডাইং) jets, stenters (স্টেন্টার), and labs — but zero digital connection between them. Management (ম্যানেজমেন্ট) had no live visibility (ভিজিবিলিটি) into what was actually happening on the floor.

▶ Our Solution:
Over four months, I built the end-to-end Data Pipeline (ডাটা পাইপলাইন) — from physical (ফিজিক্যাল) sensors (সেন্সর) all the way to the cloud (ক্লাউড). Using MQTT (এম-কিউ-টি-টি), every machine's live state is synchronized (সিঙ্ক্রোনাইজড) into our Digital Twin (ডিজিটাল টুইন) engine. On top of that, we added AI automation (এ-আই অটোমেশন) for fabric defect (ডিফেক্ট) inspection (ইন্সপেকশন) and color recipe calculation (ক্যালকুলেশন).

▶ The Result:
If you look at the right side of the slide, that's our live Digital Twin HUD (এইচ-ইউ-ডি). Machine temperature and speed update here in under 25 milliseconds (মিলিসেকেন্ড), and this system is running 24/7 in real production (প্রোডাকশন) right now."

--------------------------------------------------------------------------------
SLIDE 02: IDENTIFYING REAL FACTORY PROBLEMS (ফ্যাক্টরির আসল সমস্যাগুলো)
[পিলার: Problem Identification]
================================================================================
স্লাইডের উদ্দেশ্য:
সিস্টেম বানানোর আগে ফ্লোরের ৪টি বাস্তব সমস্যা সহজ ভাষায় তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Before writing a single line of code, we spent time on the factory floor to pinpoint (পিন-পয়েন্ট) the real bottlenecks (বটলনেক). To be honest, we found four major problems:

First, too much manual (ম্যানুয়াল) work. Lab technicians (টেকনিশিয়ান) were calculating (ক্যালকুলেটিং) dye formulas (ফর্মুলা) by hand, and supervisors (সুপারভাইজার) were writing machine readings into paper notebooks. You know, that's slow and very prone (প্রোন) to human error.

Second, disconnected (ডিসকানেক্টেড) machines. Each machine was working like an isolated (আইসোলেটেড) island. If one chamber overheated, nobody in the next department knew about it.

Third, missing live data. Factory directors (ডিরেক্টর) didn't have real-time numbers — they only got reports at the end of the shift or once a week.

And fourth, delayed reaction (রিঅ্যাকশন) cost. By the time someone noticed a shade problem or fabric burning, an entire (এনটায়ার) 10,000-meter batch (ব্যাচ) could already be ruined.

▶ Our Goal:
So, our main objective (অবজেক্টিভ) was clear: replace guesswork (গেস-ওয়ার্ক) with a live, data-driven (ডাটা-ড্রিভেন) Digital Twin (ডিজিটাল টুইন) of the whole factory."

--------------------------------------------------------------------------------
SLIDE 03: OUR UNIFIED SOLUTION (পাঁচটি মডিউলের সমন্বিত সমাধান)
[পিলার: Solution Overview & Architecture]
================================================================================
স্লাইডের উদ্দেশ্য:
৫টি সহজ মডিউলের মাধ্যমে পুরো সমাধানকে পরিষ্কারভাবে উপস্থাপন করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"To solve this without replacing any expensive (এক্সপেন্সিভ) hardware, we designed AutoTaskX (অটো-টাস্ক-এক্স) around five modular (মডিউলার) engines that all share one unified (ইউনিফাইড) data pipeline (ডাটা পাইপলাইন):

Number one, Color Formulation (কালার ফর্মুলেশন) — which automates (অটোমেটস) lab dye math instead of trial-and-error.
Number two, Visual Quality Inspection (ইন্সপেকশন) — using cameras and AI automation (এ-আই অটোমেশন) to catch fabric defects (ডিফেক্ট) immediately (ইমিডিয়েটলি).
Number three, Production Intelligence (ইন্টেলিজেন্স) — tracking machine runtime, OEE (ও-ই-ই), and heat anomalies (অ্যানোমালিস).
Number four, Textile OS & Digital Twin (টেক্সটাইল ও-এস অ্যান্ড ডিজিটাল টুইন) — and this is really the heart of my work. It connects physical (ফিজিক্যাল) PLCs (পি-এল-সি) and sensors (সেন্সর) to keep a live virtual (ভার্চুয়াল) copy of every machine.
And number five, ERP Integration (ই-আর-পি ইন্টিগ্রেশন) — syncing shopfloor output directly with SAP (এস-এ-পি) or Datatex (ডাটাটেক্স).

The beauty of this setup (সেটআপ) is that every department gets its own clean tool, while everything stays synchronized (সিঙ্ক্রোনাইজড) underneath."

--------------------------------------------------------------------------------
SLIDE 04: END-TO-END DATA PIPELINE (সেন্সর থেকে ড্যাশবোর্ডে ডাটা যাত্রা)
[পিলার: Data Engineering & MQTT Pipeline]
================================================================================
স্লাইডের উদ্দেশ্য:
একজন Data Engineer হিসেবে ৪-ধাপের ডাটা পাইপলাইন সহজ ও স্মার্টভাবে ব্যাখ্যা করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"As a Digital Twin & Data Engineer, my core job was building a clean, reliable (রিলায়েবল) data pipeline (ডাটা পাইপলাইন) from the shopfloor to the screen. Let me break it down into four simple steps:

Step one is Sense (সেন্স) — industrial (ইন্ডাস্ট্রিয়াল) sensors (সেন্সর) like PT100 (পি-টি হান্ড্রেড) temperature probes (প্রোব) and 16K line-scan cameras capture raw physical (ফিজিক্যাল) signals.

Step two is Connect (কানেক্ট) — our local Edge Gateway (এজ গেটওয়ে) cleans that raw signal into standard JSON (জে-সন) format and pushes it over MQTT (এম-কিউ-টি-টি) to our EMQX Broker (ই-এম-কিউ-এক্স ব্রোকার).

Step three is Process (প্রসেস) — our FastAPI (ফাস্ট-এ-পি-আই) backend receives the MQTT stream, validates (ভ্যালিডেটস) the data, updates the live Digital Twin (ডিজিটাল টুইন) state, and writes the history into TimescaleDB (টাইম-স্কেল-ডি-বি).

Step four is Deliver (ডেলিভার) — WebSockets (ওয়েব-সকেট) immediately (ইমিডিয়েটলি) push those updates to the Next.js (নেক্সট-জে-এস) dashboard.

You know, from a sensor changing temperature on a machine to the manager seeing it on screen — the whole journey takes less than 25 milliseconds (মিলিসেকেন্ড)."

--------------------------------------------------------------------------------
SLIDE 05: FEATURE 01 — COLOR FORMULATION (স্মার্ট কালার ফর্মুলেশন)
[পিলার: Problem Solving & Automated Chemistry]
================================================================================
স্লাইডের উদ্দেশ্য:
ল্যাবরেটরির রঙ মেলানোর সমস্যা কীভাবে ম্যাথ ও অটোমেশন দিয়ে সলভ হয়েছে তা বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Let's look at Feature one — Color Formulation (কালার ফর্মুলেশন).

▶ The Problem:
In textile dyeing (ডাইং), matching a buyer's color sample on the first try is honestly (অনেস্টলি) quite tough. Traditionally (ট্র্যাডিশনালি), chemists (কেমিস্ট) spent 5 to 6 hours mixing and testing batches (ব্যাচেস) manually, wasting a lot of expensive (এক্সপেন্সিভ) dyes and water.

▶ Our Solution:
Here, we automated (অটোমেটেড) the calculation (ক্যালকুলেশন) using Kubelka-Munk (কুবেলকা-মাঙ্ক) optical (অপটিক্যাল) math. First, a Spectrophotometer (স্পেকট্রো-ফোটোমিটার) scans the target fabric and reads its light wavelength (ওয়েভলেংথ). Then our engine calculates (ক্যালকুলেটস) the exact grams of reactive (রিঅ্যাক্টিভ) dye needed per 100 kilograms and sends instructions to the auto-dispenser (অটো-ডিস্পেন্সার). Of course, for safety, the lab still does a quick beaker (বিকার) validation (ভ্যালিডেশন) check before bulk production (প্রোডাকশন).

▶ The Result:
Color variance — what we call Delta-E (ডেল্টা-ই) — stays under 1.0, which looks like a perfect match to the human eye, and first-pass lab success jumped to over 85%."

--------------------------------------------------------------------------------
SLIDE 06: FEATURE 02 — AI VISION INSPECTION (এ-আই ভিত্তিক কাপড়ের মান পরীক্ষা)
[পিলার: AI Automation & Quality Control]
================================================================================
স্লাইডের উদ্দেশ্য:
কাপড়ের ডিফেক্ট ধরতে AI Automation কীভাবে কাজ করে তা সহজ ভাষায় তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Moving on to Feature two — Visual Quality Inspection (ইন্সপেকশন) powered by AI automation (এ-আই অটোমেশন).

▶ The Problem:
Think about it — when fabric moves at 80 to 120 meters per minute on a finishing (ফিনিশিং) machine, no human eye can reliably (রিলায়েবলি) catch tiny broken yarns or oil spots under half a millimeter (মিলিমিটার). Plus, photos taken on personal phones used to get lost with zero audit (অডিট) trail.

▶ Our Solution:
So, we integrated (ইন্টিগ্রেটেড) two camera inputs into one unified (ইউনিফাইড) AI model:
First, an industrial (ইন্ডাস্ট্রিয়াল) Basler (বাসলার) 16K line-scan camera mounted right above the fabric line.
And second, a mobile app for floor auditors (অডিটর) to do quick spot checks.

As soon as frames come in, OpenCV (ওপেন-সি-ভি) buffers (বাফারস) the strip and our YOLO (ইয়োলো) vision model automatically (অটোমেটিক্যালি) draws bounding boxes around defects (ডিফেক্ট) smaller than 0.5 millimeters (মিলিমিটার) and classifies (ক্লাসিফাইস) what type of flaw it is.

▶ The Result:
Every single meter gets consistent (কনসিস্টেন্ট), automated (অটোমেটেড) inspection (ইন্সপেকশন) with a full digital quality record."

--------------------------------------------------------------------------------
SLIDE 07: KEY CHALLENGE & SOLUTION — IMAGE & DATA OFFLOADING (বড় ছবি বনাম সার্ভার স্পিড)
[পিলার: Data Engineering Deep Dive & System Design]
================================================================================
স্লাইডের উদ্দেশ্য:
একজন Data Engineer হিসেবে ২০ মেগাবাইটের ছবি আর ছোট সেন্সর ডাটা আলাদা রাখার আর্কিটেকচার বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Now, this slide is actually my favorite engineering deep-dive because it shows how we solved a classic (ক্লাসিক) data bottleneck (বটলনেক).

▶ The Problem:
Each raw uncompressed (আনকম্প্রেসড) TIFF (টিফ) image from the 16K camera is around 20 megabytes (মেগাবাইট). To be honest, if we pushed 20-megabyte images every second through our FastAPI (ফাস্ট-এ-পি-আই) server or our MQTT Broker (এম-কিউ-টি-টি ব্রোকার), server memory and network bandwidth (ব্যান্ডউইথ) would crash within minutes.

▶ Our Solution:
So, following this UML sequence (সিকোয়েন্স) diagram (ডায়াগ্রাম), I built a parallel (প্যারালাল) offloading (অফলোডিং) pipeline:
First, the Edge PC (এজ পি-সি) asks FastAPI (ফাস্ট-এ-পি-আই) for a temporary Pre-signed S3 URL (প্রি-সাইনড এস-থ্রি ইউ-আর-এল).
Then, the Edge PC completely bypasses (বাইপাসেস) our API server and uploads that heavy 20-megabyte image directly to AWS S3 (এ-ডব্লিউ-এস এস-থ্রি).
At the exact same moment, in parallel (প্যারালাল), the Edge PC sends only tiny scan metadata (মেটাডাটা) and AI defect alerts over MQTT (এম-কিউ-টি-টি).
FastAPI simply saves the image link in PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) and notifies (নোটিফাইস) the Next.js (নেক্সট-জে-এস) frontend via WebSockets (ওয়েব-সকেট).

▶ The Result:
Zero heavy file load on our backend, and zero memory bottlenecks (বটলনেক) even during peak production (প্রোডাকশন)."

--------------------------------------------------------------------------------
SLIDE 08: PRODUCTION INTELLIGENCE & AI ANOMALY ALERT (লাইভ মেশিন মনিটরিং ও দুর্ঘটনা রোধ)
[পিলার: Real-time Digital Twin & Safety Automation]
================================================================================
স্লাইডের উদ্দেশ্য:
রিয়েল-টাইম মনিটরিং ও অটোমেটেড অ্যালার্ট কীভাবে বড় ক্ষতি ঠেকায় তা বাস্তব উদাহরণ দিয়ে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Let's talk about Feature three — Production Intelligence (ইন্টেলিজেন্স), and a very real scenario (সিনারিও) on the floor.

▶ The Problem:
On a Stenter (স্টেন্টার) machine, the safe operating limit for certain fabrics is 185 degrees Celsius (সেলসিয়াস). If the chamber suddenly spikes (স্পাইকস) to 192 degrees, the fabric can start burning or yellowing within minutes. Before AutoTaskX, operators only realized it after hundreds of meters were damaged.

▶ Our Solution:
Because temperature readings stream through MQTT (এম-কিউ-টি-টি) into our Digital Twin (ডিজিটাল টুইন) every second, the moment the sensor crosses 185 degrees and hits 192:
First, our anomaly detection (অ্যানোমালি ডিটেকশন) logic immediately (ইমিডিয়েটলি) flags the machine in red on the dashboard.
Second, an automated (অটোমেটেড) SMS alert reaches the shift supervisor (সুপারভাইজার) within 3 seconds.
And third, the supervisor opens the temperature history chart, sees exactly when the heat started drifting, and adjusts the machine right away.

▶ The Result:
That instant (ইনস্ট্যান্ট) warning saves entire (এনটায়ার) fabric lots from burning and cuts down unplanned downtime (আনপ্ল্যানড ডাউনটাইম) significantly (সিগনিফিক্যান্টলি)."

--------------------------------------------------------------------------------
SLIDE 09: TEXTILE OS & DIGITAL TWIN CORE (ভিন্ন ভিন্ন মেশিনকে এক ডিজিটাল টুইনে আনা)
[পিলার: Digital Twin Architecture — Core Focus]
================================================================================
স্লাইডের উদ্দেশ্য:
বিভিন্ন ব্র্যান্ড ও পুরোনো মেশিনকে একত্র করে কীভাবে একটি ইউনিফাইড Digital Twin তৈরি করা হয়েছে তা বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"This slide covers the core Digital Twin (ডিজিটাল টুইন) layer I built — we call it Textile OS (টেক্সটাইল ও-এস).

▶ The Problem:
You know, on a real textile floor, machines don't speak one language. You have modern German Monforts (মনফোর্টস) stenters, Italian machines, and sometimes 30-year-old controllers (কন্ট্রোলার). Some speak Modbus (মডবাস), some speak Siemens S7 (সিমেন্স এস-সেভেন), others use OPC-UA (ও-পি-সি ইউ-এ) or RS-485 (আর-এস ফোর-এইটি-ফাইভ). Bringing all of them into one system is normally a huge headache.

▶ Our Solution:
So I engineered (ইঞ্জিনিয়ার্ড) Textile OS as a universal normalization (নরমালাইজেশন) layer.
Our Edge Gateways (এজ গেটওয়ে) read each machine in its own native protocol (প্রোটোকল) — temperature, humidity (হিউমিডিটি), steam pressure, speed, and 3-phase power.
At the edge, we normalize (নরমালাইজ) all those different signals into one clean, standard JSON schema (জে-সন স্কিমা).
That clean stream continuously (কন্টিনিউয়াসলি) updates a live virtual (ভার্চুয়াল) model — a true Digital Twin (ডিজিটাল টুইন) — for every machine in the backend.

▶ The Result:
Whether a machine is brand new or 30 years old, inside AutoTaskX every machine acts like one standardized (স্ট্যান্ডার্ডাইজড) Digital Twin node."

--------------------------------------------------------------------------------
SLIDE 10: IOT DATA TRACE UNDER 25MS (একটি সেন্সর রিডিংয়ের ২৫ মিলিসেকেন্ডের যাত্রা)
[পিলার: Data Pipeline Latency & Performance]
================================================================================
স্লাইডের উদ্দেশ্য:
একটি সিঙ্গেল রিডিংয়ের <25ms এন্ড-টু-এন্ড যাত্রা সহজভাবে ধাপে ধাপে দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"As a Data Engineer, low latency (লেইটেন্সি) is something I care deeply about. So let's trace just one single temperature reading from start to finish:

First, inside Stenter zone four, a PT100 (পি-টি হান্ড্রেড) sensor reads 185.5 degrees Celsius every 100 milliseconds (মিলিসেকেন্ড).
Next, the IoT Gateway (আই-ও-টি গেটওয়ে) converts that analog (অ্যানালগ) signal into a tiny MQTT (এম-কিউ-টি-টি) packet (প্যাকেট).
It travels across the factory local network to our FastAPI (ফাস্ট-এ-পি-আই) backend.
AutoTaskX checks the safety threshold (থ্রেশহোল্ড), updates the Digital Twin (ডিজিটাল টুইন), writes it to TimescaleDB (টাইম-স্কেল-ডি-বি), and pushes it to the manager's live screen.

In fact, if we click 'Animate Data Flow' right here, you can see all six hops happen in under 25 milliseconds (মিলিসেকেন্ড). It feels completely instant (ইনস্ট্যান্ট) on the dashboard."

--------------------------------------------------------------------------------
SLIDE 11: WHY MQTT? DATA TRANSPORT DECISION (এম-কিউ-টি-টি কেন ব্যবহার করলাম?)
[পিলার: MQTT Architecture & Protocol Choice]
================================================================================
স্লাইডের উদ্দেশ্য:
সেন্সরের জন্য HTTP-র বদলে MQTT এবং ছবির জন্য HTTPS S3 বেছে নেওয়ার পরিষ্কার যুক্তি দেওয়া।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"A question I often get in technical interviews is: why use MQTT (এম-কিউ-টি-টি) instead of standard HTTP REST APIs (রেস্ট এ-পি-আই)?

▶ The Problem:
Imagine 50 machines sending sensor readings every second over standard HTTP (এইচ-টি-টি-পি). HTTP has heavy headers (হেডার) and constant connection overhead (ওভারহেড). On a noisy factory Wi-Fi (ওয়াই-ফাই) network, that slows things down and drops packets (প্যাকেট).

▶ Our Solution:
So I enforced (এনফোর্সড) two strict (স্ট্রিক্ট) rules in our architecture (আর্কিটেকচার):
Rule one: Small sensor telemetry (টেলেমেট্রি) goes through our EMQX MQTT Broker (ই-এম-কিউ-এক্স এম-কিউ-টি-টি ব্রোকার). Since temperature or RPM is only a few bytes, MQTT's tiny 2-byte header and Pub/Sub (পাব/সাব) model stream data reliably (রিলায়েবলি) into our Digital Twin (ডিজিটাল টুইন) without dropping readings.
Rule two: Large 20-megabyte images NEVER touch MQTT. They go directly over HTTPS (এইচ-টি-টি-পি-এস) to AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) so the broker (ব্রোকার) never gets blocked.

▶ The Result:
We get fast, lightweight, rock-solid (রক-সলিড) communication (কমিউনিকেশন) across the entire (এনটায়ার) factory."

--------------------------------------------------------------------------------
SLIDE 12: STORAGE ARCHITECTURE (তিনটি বিশেষায়িত ডেটাবেজ কেন?)
[পিলার: Data Engineering & Polyglot Storage]
================================================================================
স্লাইডের উদ্দেশ্য:
ডেটার ধরন অনুযায়ী ৩টি আলাদা স্টোরেজ ব্যবহার করার কারণ সহজভাবে ব্যাখ্যা করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"From a Data Engineering standpoint (স্ট্যান্ডপয়েন্ট), putting every type of data into one database is a mistake. So we use three specialized (স্পেশালাইজড) storage systems, each doing one job well:

First, PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) for relational (রিলেশনাল) business data — things like buyer orders, user roles, machine profiles, and dye recipes that need strict ACID (অ্যাসিড) accuracy (অ্যাকিউরেসি).

Second, TimescaleDB (টাইম-স্কেল-ডি-বি) for time-series (টাইম-সিরিজ) sensor data. Because we collect millions of timestamped (টাইমস্ট্যাম্পড) readings, a regular table gets super slow. TimescaleDB runs on top of PostgreSQL using Hypertables (হাইপার-টেবলস) — it automatically (অটোমেটিক্যালি) chunks data by time and gives us up to 95% compression (কম্প্রেশন).

And third, AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) for heavy files — like high-resolution (হাই-রেজোলিউশন) fabric defect scans and PDF reports.

So when a manager opens a batch history, all three work together smoothly without slowing each other down."

--------------------------------------------------------------------------------
SLIDE 13: REAL-TIME DELIVERY PIPELINE (লাইভ আপডেট বনাম হিস্টোরিক্যাল রিপোর্ট)
[পিলার: Data Serving & User Experience]
================================================================================
স্লাইডের উদ্দেশ্য:
অপারেটরের লাইভ স্ক্রিন আর ম্যানেজমেন্টের ভারী রিপোর্টের মধ্যে সার্ভার লোড কীভাবে আলাদা করা হয়েছে তা দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Once data is stored, serving (সার্ভিং) it efficiently (এফিশিয়েন্টলি) to different users is just as important.

▶ The Problem:
Floor operators (অপারেটর) need zero-lag live updates — they shouldn't have to refresh (রিফ্রেশ) their browser. Meanwhile, plant directors (ডিরেক্টর) run heavy historical (হিস্টোরিক্যাল) charts across weeks of shift data. If both share one pathway (পাথওয়ে), a heavy report could freeze the live screen.

▶ Our Solution:
So I split data delivery (ডেলিভারি) into two lanes:
For live monitoring, FastAPI WebSockets (ফাস্ট-এ-পি-আই ওয়েব-সকেট) push Digital Twin (ডিজিটাল টুইন) state changes straight to the Next.js (নেক্সট-জে-এস) dashboard without polling (পোলিং).
For historical (হিস্টোরিক্যাল) trends and shift analytics (অ্যানালিটিক্স), we use cached REST APIs (রেস্ট এ-পি-আই) powered by TimescaleDB aggregates (অ্যাগ্রিগেটস).

▶ The Result:
Even if a director loads a 30-day energy report, the operator's live machine monitor stays completely smooth with zero lag."

--------------------------------------------------------------------------------
SLIDE 14: FEATURE 05 — ERP INTEGRATION (ফ্যাক্টরি থেকে অফিসের ই-আর-পি অটোমেশন)
[পিলার: Enterprise Data Integration]
================================================================================
স্লাইডের উদ্দেশ্য:
শপফ্লোরের সাথে এন্টারপ্রাইজ ERP (SAP, Datatex, Infor)-এর স্বয়ংক্রিয় সংযোগ দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Feature five solves a very common disconnect (ডিসকানেক্ট) between the factory floor and the head office.

▶ The Problem:
Almost every big factory uses an ERP (ই-আর-পি) like SAP (এস-এ-পি), Datatex NOW (ডাটাটেক্স নাউ), or Infor M3 (ইনফর এম-থ্রি). But normally, someone writes production (প্রোডাকশন) logs on paper, and office staff type them into the ERP one or two days later — often with mistakes.

▶ Our Solution:
I built a two-way ERP bridge:
Work orders come down automatically (অটোমেটিক্যালি) from the ERP into AutoTaskX as digital jobs.
And when a dyeing (ডাইং) or inspection (ইন্সপেকশন) batch finishes, actual meters produced and exact chemical amounts used sync straight back up into the ERP inventory (ইনভেন্টরি).

▶ The Result:
No more two-day reporting delays, no manual data entry errors, and 100% transparent (ট্রান্সপারেন্ট) inventory tracking."

--------------------------------------------------------------------------------
SLIDE 15: COMPLETE 4-ZONE ARCHITECTURE (পুরো সিস্টেমের ৪-জোন আর্কিটেকচার)
[পিলার: System Architecture & Scalability]
================================================================================
স্লাইডের উদ্দেশ্য:
৪টি জোনে পুরো আর্কিটেকচারের স্কেলেবিলিটি ও ক্লিন ডিজাইন তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"This slide puts the whole architecture (আর্কিটেকচার) together in four clean zones:

Zone one is the Physical Factory (ফিজিক্যাল ফ্যাক্টরি) — stenters, dyeing machines, looms (লুমস), cameras, and over 100 sensors (সেন্সর).
Zone two is the Connection Layer — Edge Gateways (এজ গেটওয়ে) reading Modbus (মডবাস) or OPC-UA (ও-পি-সি ইউ-এ), connected to our central EMQX MQTT Broker (ই-এম-কিউ-এক্স এম-কিউ-টি-টি ব্রোকার).
Zone three is the Core & Storage Layer — our FastAPI (ফাস্ট-এ-পি-আই) backend, AI vision models, Digital Twin (ডিজিটাল টুইন) state, and our three databases: PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল), TimescaleDB (টাইম-স্কেল-ডি-বি), and AWS S3 (এ-ডব্লিউ-এস এস-থ্রি).
Zone four is Delivery & Enterprise (এন্টারপ্রাইজ) — the Next.js dashboard, mobile QA app, SMS alerts, and the ERP bridge.

And the best part is, this architecture is loosely coupled (লুজলি কাপল্ড). If the client adds 50 more machines in another building tomorrow, we just plug in new gateways in Zones one and two — zero core code changes needed."

--------------------------------------------------------------------------------
SLIDE 16: MEASURABLE BUSINESS OUTCOMES (গাজীপুর মিলে বাস্তব ফলাফল ও আরওআই)
[পিলার: Outcomes & Business ROI]
================================================================================
স্লাইডের উদ্দেশ্য:
গাজীপুর টেক্সটাইল মিলে পাওয়া বাস্তব ও পরিমাপযোগ্য ফলাফলগুলো তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"At the end of the day, great engineering has to show real business results. On this slide, you're looking at a live snapshot (স্ন্যাপশট) from Gazipur (গাজীপুর) Textile Mill number four:

Out of 26 connected machines, 24 are running non-stop right now, and 2 are offline for scheduled (স্কেজুয়ালড) maintenance (মেইনটেন্যান্স) — so nothing is a surprise anymore.
Stenter temperature is holding steady at 185.5 degrees with zero critical alerts.
In a single day, we tracked 42,500 meters of fabric in real time.
With AI vision inspection (ইন্সপেকশন), the Right-First-Time (রাইট-ফার্স্ট-টাইম) quality pass rate reached 99.2%.
And overall (ওভারঅল) equipment effectiveness (ইফেক্টিভনেস) — or OEE (ও-ই-ই) — improved by 14% within just four months.

The factory owner can literally (লিটারালি) open a tablet from anywhere in the world and see how the entire (এনটায়ার) plant is performing."

--------------------------------------------------------------------------------
SLIDE 17: AI AUTOMATION & FUTURE ROADMAP (এ-আই অটোমেশন ও ভবিষ্যৎ পরিকল্পনা)
[পিলার: AI Automation & Future Scalability]
================================================================================
স্লাইডের উদ্দেশ্য:
AI Automation ও Predictive Maintenance-এর মাধ্যমে সিস্টেমটিকে কীভাবে আরও স্মার্ট করা হচ্ছে তা দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Because we built such a clean data foundation (ফাউন্ডেশন), adding deeper AI automation (এ-আই অটোমেশন) next becomes really straightforward (স্ট্রেইট-ফরওয়ার্ড). Here is our five-stage roadmap (রোডম্যাপ):

Stage one is Connect More — expanding (এক্সপ্যান্ডিং) IoT gateways across spinning, weaving, and knitting sheds for 100% floor visibility (ভিজিবিলিটি).
Stage two is Automated (অটোমেটেড) Inspection (ইন্সপেকশন) — adding automatic camera triggers (ট্রিগারস) on unrolling (আনরোলিং) frames so every meter is scanned hands-free.
Stage three is Historical AI Analytics (অ্যানালিটিক্স) — using months of TimescaleDB (টাইম-স্কেল-ডি-বি) data to predict (প্রিডিক্ট) seasonal dye behavior.
Stage four is Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স) — analyzing (অ্যানালাইজিং) motor vibration (ভাইব্রেশন) and bearing heat patterns so AI warns engineers before a machine breaks down.
And stage five is Closed-Loop Control — where the Digital Twin (ডিজিটাল টুইন) can safely send automated adjustments back to the PLC (পি-এল-সি) to fine-tune (ফাইন-টিউন) machine speed or heat automatically."

--------------------------------------------------------------------------------
SLIDE 18: CONCLUSION & Q&A (সমাপ্তি ও প্রশ্নোত্তর পর্ব)
[পিলার: Closing Statement]
================================================================================
স্লাইডের উদ্দেশ্য:
আত্মবিশ্বাসের সাথে প্রেজেন্টেশন শেষ করা এবং টেকনিক্যাল প্রশ্নোত্তরের জন্য ফ্লোর ওপেন করা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"To wrap up, AutoTaskX (অটো-টাস্ক-এক্স) isn't a classroom concept or a mockup (মক-আপ). It's a live, 24/7 Industrial IoT and Digital Twin (ডিজিটাল টুইন) platform built in four months and running on a real factory floor today.

Combining (কম্বাইনিং) my Computer Science background from BUBT (বি-ইউ-বি-টি) with hands-on work in Data Engineering, MQTT (এম-কিউ-টি-টি), Digital Twin architecture (আর্কিটেকচার), and AI automation (এ-আই অটোমেশন), I focused on keeping the system simple, fast, and reliable (রিলায়েবল).

Thank you so much for your time and attention. I'd love to answer any technical questions you have about our Digital Twin setup, MQTT pipeline, storage design, or AI workflow."

================================================================================
MASTER CHEAT SHEET: ৬টি গুরুত্বপূর্ণ ইন্টারভিউ প্রশ্ন ও সাবলীল ইংরেজি উত্তর
================================================================================

প্রশ্ন ১: "How do you keep the Digital Twin (ডিজিটাল টুইন) always synchronized (সিঙ্ক্রোনাইজড) with the physical machines?"
স্মার্ট উত্তর:
"You know, every physical (ফিজিক্যাল) machine has an Edge Gateway (এজ গেটওয়ে) polling (পোলিং) sensors every 100 milliseconds (মিলিসেকেন্ড). It normalizes (নরমালাইজেস) the reading into standard JSON (জে-সন) and publishes (পাবলিশেস) it over MQTT (এম-কিউ-টি-টি) to our EMQX Broker (ই-এম-কিউ-এক্স ব্রোকার). Our FastAPI (ফাস্ট-এ-পি-আই) backend receives that stream immediately (ইমিডিয়েটলি), updates the Digital Twin state in memory, saves history to TimescaleDB (টাইম-স্কেল-ডি-বি), and pushes live updates over WebSockets (ওয়েব-সকেট) — all in under 25 milliseconds."

প্রশ্ন ২: "Why did you choose MQTT instead of regular HTTP REST APIs for sensor data?"
স্মার্ট উত্তর:
"To be honest, HTTP (এইচ-টি-টি-পি) is great for normal web requests, but for high-frequency sensor data, opening and closing HTTP connections with large headers (হেডার) wastes a lot of bandwidth (ব্যান্ডউইথ). MQTT (এম-কিউ-টি-টি) only uses a tiny 2-byte header on one persistent (পারসিস্টেন্ট) connection. Plus, with QoS Level 1 (কিউ-ও-এস লেভেল ওয়ান), even if the factory Wi-Fi flickers (ফ্লিকারস), we don't lose critical (ক্রিটিক্যাল) machine readings."

প্রশ্ন ৩: "Why TimescaleDB? Why not just plain PostgreSQL or MongoDB?"
স্মার্ট উত্তর:
"Actually, we needed both worlds. Our orders and dye recipes are strictly (স্ট্রিক্টলি) relational (রিলেশনাল), so PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) gives us solid ACID (অ্যাসিড) reliability (রিলায়াবিলিটি). But storing millions of sensor rows in a plain table slows queries (কুয়েরিস) down over time. Since TimescaleDB (টাইম-স্কেল-ডি-বি) runs right inside PostgreSQL using Hypertables (হাইপার-টেবলস), we get automatic (অটোমেটিক) time partitioning (পার্টিশনিং) and 95% storage compression (কম্প্রেশন) without managing two separate database engines."

প্রশ্ন ৪: "What happens if the factory internet drops while uploading a 20MB inspection image?"
স্মার্ট উত্তর:
"That's a very real factory challenge, and we planned for it right away. On the Edge PC (এজ পি-সি), we implemented (ইমপ্লিমেন্টেড) a local FIFO disk buffer (ফিফো ডিস্ক বাফার) and queue (কিউ). Every image is written to local storage first, and it is never deleted until AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) confirms a successful 200 OK upload. As soon as the internet comes back, pending (পেন্ডিং) images sync automatically (অটোমেটিক্যালি) in exact order — zero lost frames."

প্রশ্ন ৫: "Why did you pick FastAPI over Django for the backend?"
স্মার্ট উত্তর:
"Basically, we had hundreds of concurrent (কনকারেন্ট) IoT streams and live WebSocket (ওয়েব-সকেট) dashboards running at the same time. Traditional (ট্র্যাডিশনাল) Django (জ্যাঙ্গো) is mostly synchronous (সিঙ্ক্রোনাস) and heavier for high-concurrency (হাই-কনকারেন্সি) streaming. FastAPI (ফাস্ট-এ-পি-আই) is built on native AsyncIO (অ্যাসিঙ্ক-আই-ও) and ASGI (এ-এস-জি-আই), so it handles many simultaneous (সাইমালটেনিয়াস) MQTT and WebSocket connections smoothly using much less CPU (সি-পি-ইউ) and RAM (র‍্যাম)."

প্রশ্ন ৬: "How is AI automation delivering real value here instead of just being a buzzword?"
স্মার্ট উত্তর:
"To be honest, we avoided adding AI just for show — we used it in three practical (প্র্যাকটিক্যাল) places: first, OpenCV (ওপেন-সি-ভি) and YOLO (ইয়োলো) catching sub-millimeter (সাব-মিলিমিটার) fabric defects at up to 120 meters per minute; second, automated (অটোমেটেড) thermal (থার্মাল) anomaly (অ্যানোমালি) alerts that prevented burning fabric at 192 degrees; and third, building clean historical (হিস্টোরিক্যাল) data in TimescaleDB (টাইম-স্কেল-ডি-বি) so we can run Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স) on motor vibrations (ভাইব্রেশন) before breakdowns happen."

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
    "01": "1. Role & Digital Twin Vision",
    "02": "1. Problem Identification",
    "03": "2. Unified Solution Overview",
    "04": "2. Data Pipeline & MQTT",
    "05": "3. AI & Spectral Chemistry",
    "06": "3. AI Vision Automation",
    "07": "4. Challenge & Data Offload",
    "08": "4. AI Anomaly & Safety",
    "09": "2. Digital Twin Core",
    "10": "2. Data Trace (<25ms)",
    "11": "5. MQTT Protocol Decision",
    "12": "5. Polyglot Data Storage",
    "13": "2. Real-time Data Serving",
    "14": "3. Enterprise ERP Bridge",
    "15": "2. 4-Zone Scalable Topology",
    "16": "6. Measurable ROI & Impact",
    "17": "2. AI & Autonomous Roadmap",
    "18": "6. Summary & Panel Q/A"
}

engineering_knowledge = {
    "01": [
        {"label": "Target Role", "val": "Digital Twin & Data Engineer (BUBT CSE)"},
        {"label": "Platform Category", "val": "Industrial IoT & Real-time Digital Twin"},
        {"label": "Telemetry Latency", "val": "< 25ms round-trip (Sensor to Web UI)"},
        {"label": "Production Proof", "val": "100% Active Production 24/7 (4-Month Client Delivery)"}
    ],
    "02": [
        {"label": "Core Problem", "val": "Manual Pen-Paper Logs & Disconnected Mill Islands"},
        {"label": "Operational Risk", "val": "Shade Variation & Delayed Shift-End Defect Discovery"},
        {"label": "Business Cost", "val": "Up to 10,000m Fabric Batch Rejection Losses"},
        {"label": "Target Objective", "val": "Real-time Data-Driven Digital Twin Visibility"}
    ],
    "03": [
        {"label": "Architecture", "val": "5 Modular Engines Sharing One Unified Data Pipeline"},
        {"label": "Core Modules", "val": "Color · Vision AI · Production · Textile OS Twin · ERP"},
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
        {"label": "Problem Solved", "val": "5-6 Hour Manual Lab Dye Trial-and-Error Waste"},
        {"label": "Solution Engine", "val": "Kubelka-Munk Spectral Math + Automated Recipe Calc"},
        {"label": "Quality Precision", "val": "CIE ΔE < 1.0 (85%+ First-Pass Match, Lab Validated)"},
        {"label": "Dispensary Sync", "val": "Exact Grams per 100kg Sent to Auto-Dispenser"}
    ],
    "06": [
        {"label": "Problem Solved", "val": "Human Eye Missing <0.5mm Flaws at 80-120 m/min"},
        {"label": "Hardware Inputs", "val": "Basler racer 2L (16K Line-Scan) + Floor Mobile App"},
        {"label": "AI Automation", "val": "OpenCV Image Stitching + YOLO Defect Classification"},
        {"label": "Audit Trail", "val": "Instant Bounding Box & Automated Roll Defect Report"}
    ],
    "07": [
        {"label": "Key Challenge", "val": "20MB Uncompressed TIFF Frames Crashing API / MQTT"},
        {"label": "My Solution", "val": "Parallel Pre-signed AWS S3 Direct Upload from Edge PC"},
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
        {"label": "Core Digital Twin", "val": "Textile OS Universal Protocol Normalization Layer"},
        {"label": "Supported Protocols", "val": "Modbus RTU/TCP, Siemens S7, OPC-UA, RS-485 Serial"},
        {"label": "Fleet Coverage", "val": "30-Year Legacy Controllers + Modern European Stenters"},
        {"label": "Virtual Sync", "val": "Unified JSON Schema Feeding Live Digital Twin Nodes"}
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
        {"label": "Problem Solved", "val": "24-48 Hour Manual Paper Delay to SAP / Datatex / Infor"},
        {"label": "Work Orders Down", "val": "ERP Orders Auto-Push as Digital Shopfloor Jobs"},
        {"label": "Output Sync Up", "val": "Actual Meters & Chemical Usage Auto-Deduct in ERP"},
        {"label": "Audit Impact", "val": "100% Paperless & Tamper-Proof Production Ledgers"}
    ],
    "15": [
        {"label": "Zone 1 & Zone 2", "val": "100+ Floor Sensors -> Edge Gateways -> EMQX MQTT"},
        {"label": "Zone 3 (Core)", "val": "FastAPI, AI Models, Digital Twin & Polyglot Storage"},
        {"label": "Zone 4 (Apps)", "val": "Next.js Dashboard, Mobile QA, SMS & ERP Connector"},
        {"label": "Scalability", "val": "Loosely Coupled — Add 50 Machines Without Code Rewrites"}
    ],
    "16": [
        {"label": "Live Deployment", "val": "Gazipur Textile Mill #04 — 26 Connected Machines"},
        {"label": "Fleet Status", "val": "24 Running Live · 2 Planned Maintenance · 0 Alerts"},
        {"label": "Daily Throughput", "val": "42,500m Tracked Live · 99.2% Vision Pass Rate (RFT)"},
        {"label": "Operational ROI", "val": "+14% OEE Improvement Achieved Within 4 Months"}
    ],
    "17": [
        {"label": "Phase 1 & 2", "val": "100% Mill Expansion + Automated Inline Trigger Rigs"},
        {"label": "Phase 3 (Analytics)", "val": "TimescaleDB Historical AI Modeling for Seasonal Shades"},
        {"label": "Phase 4 (AI PdM)", "val": "Vibration & Bearing Heat AI Predictive Maintenance"},
        {"label": "Phase 5 (Autonomy)", "val": "Closed-Loop Digital Twin Feedback to Adjust PLC Speed"}
    ],
    "18": [
        {"label": "Core Identity", "val": "Digital Twin & Data Engineer (BUBT CSE Graduate)"},
        {"label": "Production Proof", "val": "4-Month Client Delivery Running 24/7 on Mill Floor"},
        {"label": "Key Pillars", "val": "Digital Twin · EMQX MQTT · Polyglot Data · AI Vision"},
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
