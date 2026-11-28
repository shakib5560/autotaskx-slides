import re
import json

# Complete slide-by-slide English presentation guide tailored for a Digital Twin & Data Engineer interview.
# Uses simple, natural, fluent, and interactive spoken English (avoiding stiff/tongue-twister words)
# while highlighting Digital Twin, MQTT, Data Engineering, AI Automation, 3-dev core team (~40-50% backend contribution),
# and the real client engagement flow (Client came to our office -> Factory visit -> Blueprint -> 4-month build).
guide_text = """================================================================================
AUTOTASKX — EASY & FLUENT ENGLISH PRESENTATION GUIDE
================================================================================
Target Role: Digital Twin & Data Engineer
Project: AutoTaskX — Industrial IoT & Real-Time Digital Twin Platform
Client: A Prominent Player in the Bangladeshi Textile Industry
Team & Contribution: 3-Developer Core Team (Backend & Frontend) · One of the Main Backend Engineers (~40–50% of total work)
Workflow: Office Consultation → Industry Visit → Requirements & Blueprint → 4-Month Live Delivery (24/7)
================================================================================

[পড়ার এবং প্রেজেন্ট করার সহজ টিপস — How to Sound Fluent & Interactive]
--------------------------------------------------------------------------------
• কঠিন সব ভারী ইংরেজি শব্দ বাদ দিয়ে একদম সহজ, সাবলীল এবং ন্যাচারাল (Natural) ইংরেজিতে সাজানো হয়েছে — যেন আপনি নির্ভয়ে ও ফ্লুয়েন্টলি (Fluently) কথা বলতে পারেন।
• আপনার আগে থেকেই নিজের পরিচয় দেওয়া থাকায় Slide 01 সরাসরি প্রজেক্ট ও ক্লায়েন্টের গল্প দিয়ে শুরু হয়েছে।
• ৩ জন ডেভেলপারের কোর টিমে (Core Team) আপনি মূল Backend Engineer-দের একজন (~৪০–৫০% কাজ করেছেন), তাই সব জায়গায় "We built / We created" ব্যবহার করা হয়েছে।
• প্রেজেন্টেশনটি ইন্টারেক্টিভ (Interactive) করতে মাঝে মাঝে ইন্টারভিউয়ারকে স্লাইডের দিকে তাকাতে বলুন এবং ছোট ছোট প্রশ্ন/হুক ব্যবহার করুন (যেমন: "If you look right here...", "You might be wondering...", "Let's trace this live...")।

================================================================================
SLIDE 01: PROJECT OVERVIEW & CLIENT VISION (প্রজেক্ট পরিচিতি ও ক্লায়েন্টের ভিশন)
[পিলার: Client Vision & Project Objectives]
================================================================================
স্লাইডের উদ্দেশ্য:
নিজের পরিচয় বাদ দিয়ে সরাসরি ক্লায়েন্ট প্রজেক্ট দিয়ে শুরু করা — ক্লায়েন্ট অফিসে এসে কী চেয়েছিলেন, ফ্যাক্টরি ভিজিটের পর আমরা কী ব্লুপ্রিন্ট বানাই এবং ৩ জনের টিমে আপনার ৪০-৫০% অবদান সহজ ও ফ্লুয়েন্ট ইংরেজিতে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Alright, let's jump right into the project — AutoTaskX (অটো-টাস্ক-এক্স). Basically (বেসিক্যালি), it's a real-time Industrial IoT (আই-ও-টি) and Digital Twin (ডিজিটাল টুইন) platform built for one of the big, prominent (প্রমিনেন্ট) names in the Bangladeshi textile industry (ইন্ডাস্ট্রি).

▶ How It Started (The Client Request):
To be honest, the way this project started was pretty interesting (ইন্টারেস্টিং). The client already knew they had big gaps in their factory, so they actually came to our office. What they really wanted was full automation (অটোমেশন) — they wanted to turn their whole factory floor into a live Digital Twin (ডিজিটাল টুইন).

▶ Industry Visit & Team Build:
So right after that meeting, we visited their factory to check out the real machines — like dyeing (ডাইং) jets, stenters (স্টেন্টার), and the color lab. From there, we listed all the requirements (রিকোয়ারমেন্টস) and created a clean software blueprint (ব্লুপ্রিন্ট). Over four months, our core team of three developers built both the backend (ব্যাকএন্ড) and frontend (ফ্রন্টএন্ড). As one of the main backend engineers, I handled around 40 to 50 percent of the total work — mostly the MQTT (এম-কিউ-টি-টি) data pipeline (পাইপলাইন), Digital Twin live updates, and AI automation (এ-আই অটোমেশন). And you know, as a backend and IoT enthusiast (এনথুজিয়াস্ট), working on live factory hardware was super exciting.

▶ The Result:
If you look at the right side of the slide right here, that's our live Digital Twin screen. Every machine updates in under 25 milliseconds (মিলিসেকেন্ড), and it's running 24/7 in live production (প্রোডাকশন) today."

--------------------------------------------------------------------------------
SLIDE 02: CLIENT PAIN POINTS & MILL REALITY (ক্লায়েন্টের সমস্যা ও ফ্যাক্টরি ভিজিটের অভিজ্ঞতা)
[পিলার: Problem Identification & Requirements]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্ট অফিসে এসে কী কী সমস্যার কথা বলেছিলেন এবং ইন্ডাস্ট্রি ভিজিটে গিয়ে আমরা কী কী বটলনেক দেখেছি তা সহজ গল্পের মতো বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"When the client first met us at our office, they shared the everyday problems slowing down their mill. Then during our factory visit, we saw these four big bottlenecks (বটলনেক) right on the floor:

First, too much manual (ম্যানুয়াল) work. Lab staff were doing color math by hand, and supervisors (সুপারভাইজার) were writing machine numbers in paper notebooks. You know, that takes forever and leads to human mistakes.

Second, machines didn't talk to each other. Every machine worked alone like an island. If one machine got too hot, nobody else knew.

Third, no live numbers for management (ম্যানেজমেন্ট). The client wanted live updates, but back then, they only saw reports at the end of a shift or once a week.

And fourth, late action cost a lot of money. By the time someone spotted a wrong shade or burnt fabric, an entire (এনটায়ার) 10,000-meter batch (ব্যাচ) was already wasted.

▶ What the Client Asked For:
So the client told us clearly: cut out the guesswork (গেস-ওয়ার্ক) and give them one live, automated (অটোমেটেড) Digital Twin (ডিজিটাল টুইন) for the whole factory."

--------------------------------------------------------------------------------
SLIDE 03: ARCHITECTURE BLUEPRINT & 5 MODULES (সফটওয়্যার ব্লুপ্রিন্ট ও পাঁচটি মডিউল)
[পিলার: Solution Blueprint & Modular Design]
================================================================================
স্লাইডের উদ্দেশ্য:
সফটওয়্যার ব্লুপ্রিন্টে থাকা ৫টি মডিউল সহজ ও সাবলীল ভাষায় ইন্টারভিউয়ারকে দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"After our factory visit, we put together a clean software blueprint (ব্লুপ্রিন্ট) so the client wouldn't have to buy new machines. Instead, we built AutoTaskX (অটো-টাস্ক-এক্স) around five connected modules (মডিউল) on top of one shared data pipeline (পাইপলাইন). Let me point them out on the slide:

One is Color Formulation (কালার ফর্মুলেশন) — which replaces manual lab trial-and-error with fast math.
Two is Visual Quality Inspection (ইন্সপেকশন) — using cameras and AI automation (এ-আই অটোমেশন) to spot fabric flaws right away.
Three is Production Intelligence (ইন্টেলিজেন্স) — watching machine runtime, efficiency (এফিশিয়েন্সি), and heat spikes.
Four is Textile OS & Digital Twin (টেক্সটাইল ও-এস অ্যান্ড ডিজিটাল টুইন) — which connects real sensors (সেন্সর) and PLCs (পি-এল-সি) to keep a live digital copy of every machine.
And five is ERP Integration (ই-আর-পি ইন্টিগ্রেশন) — sending factory output straight into SAP (এস-এ-পি) or Datatex (ডাটাটেক্স).

You know, each team gets its own simple dashboard (ড্যাশবোর্ড), while all five modules stay in sync behind the scenes."

--------------------------------------------------------------------------------
SLIDE 04: END-TO-END DATA PIPELINE (সেন্সর থেকে ড্যাশবোর্ডে ডাটা যাত্রা)
[পিলার: Data Engineering & MQTT Pipeline]
================================================================================
স্লাইডের উদ্দেশ্য:
একজন Data Engineer হিসেবে ৪ ধাপের ডাটা ফ্লো (Sense → Connect → Process → Deliver) খুব সহজ করে বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Now, if you look at these four steps on the slide, this is our core Data Pipeline (ডাটা পাইপলাইন) — the heart of the Digital Twin (ডিজিটাল টুইন). Let's walk through it together:

Step one is Sense (সেন্স). Sensors (সেন্সর) and high-speed cameras on the client's machines capture temperature (টেম্পারেচার), speed, and fabric images.

Step two is Connect (কানেক্ট). Our Edge Gateway (এজ গেটওয়ে) converts (কনভার্টস) that raw signal into clean JSON (জে-সন) and sends it over MQTT (এম-কিউ-টি-টি) to our EMQX Broker (ই-এম-কিউ-এক্স ব্রোকার).

Step three is Process (প্রসেস). Our FastAPI (ফাস্ট-এ-পি-আই) backend picks up the MQTT stream, checks the data, updates the Digital Twin state, and saves the history in TimescaleDB (টাইম-স্কেল-ডি-বি).

Step four is Deliver (ডেলিভার). WebSockets (ওয়েব-সকেট) push the live update straight to our Next.js (নেক্সট-জে-এস) screen.

To be honest, from a machine changing heat on the floor to the client seeing it on screen — the whole trip takes less than 25 milliseconds (মিলিসেকেন্ড)."

--------------------------------------------------------------------------------
SLIDE 05: FEATURE 01 — COLOR FORMULATION (স্মার্ট কালার ফর্মুলেশন)
[পিলার: Client Lab Automation]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের ডাইং ল্যাবের রঙ মেলানোর সমস্যা কীভাবে ম্যাথ ও অটোমেশন দিয়ে সলভ হলো তা বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Let's look at Feature one — Color Formulation (কালার ফর্মুলেশন).

▶ What the Client Faced:
When we visited the client's dye lab, matching (ম্যাচিং) a buyer's color sample on the first try was a big bottleneck (বটলনেক). Lab chemists (কেমিস্ট) spent 5 to 6 hours mixing test batches (ব্যাচেস) by hand, wasting a lot of dyes and water. The client really wanted to automate (অটোমেট) this step.

▶ Our Solution:
So we built a smart recipe engine using Kubelka-Munk (কুবেলকা-মাঙ্ক) color math. First, a color scanner — a Spectrophotometer (স্পেকট্রো-ফোটোমিটার) — reads the target fabric. Then our engine calculates (ক্যালকুলেটস) the exact grams of dye needed per 100 kg and sends it to the auto-dispenser (অটো-ডিস্পেন্সার). For safety, the lab still does a quick beaker (বিকার) check before bulk dyeing (ডাইং).

▶ The Result:
Color difference — called Delta-E (ডেল্টা-ই) — stays under 1.0, which looks like a dead-on match to the human eye, and first-try lab success went past 85 percent."

--------------------------------------------------------------------------------
SLIDE 06: FEATURE 02 — AI VISION INSPECTION (এ-আই ভিত্তিক কাপড়ের মান পরীক্ষা)
[পিলার: AI Automation & Quality Control]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের ফ্লোরে কাপড়ের ডিফেক্ট ধরতে AI Automation কীভাবে কাজ করে তা সহজ ও সাবলীলভাবে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Now look at Feature two — Visual Quality Inspection (ইন্সপেকশন) using AI automation (এ-আই অটোমেশন).

▶ What the Client Wanted:
Think about it — when fabric flies through a machine at 80 to 120 meters per minute, human eyes simply can't catch tiny broken yarns or oil spots smaller than half a millimeter (মিলিমিটার). Also, workers used to take photos on personal phones and lose them. The client wanted an automatic, digital way to check every meter.

▶ Our Solution:
So we connected two camera sources into one AI vision model:
First, a fast Basler (বাসলার) 16K line-scan camera mounted right over the fabric line.
And second, a mobile app for floor checkers to snap quick spot photos.

As frames come in, OpenCV (ওপেন-সি-ভি) prepares the fabric strip, and our YOLO (ইয়োলো) AI model draws boxes around any flaw smaller than 0.5 millimeters (মিলিমিটার) and tags what kind of defect (ডিফেক্ট) it is.

▶ The Result:
Now every meter gets checked on its own with a clean digital report — no more guesswork (গেস-ওয়ার্ক)."

--------------------------------------------------------------------------------
SLIDE 07: KEY CHALLENGE & SOLUTION — IMAGE & DATA OFFLOADING (বড় ছবি বনাম সার্ভার স্পিড)
[পিলার: Data Engineering Deep Dive & System Design]
================================================================================
স্লাইডের উদ্দেশ্য:
২০ মেগাবাইটের ভারী ছবি আর ছোট সেন্সর ডাটা আলাদা রেখে আমরা কীভাবে সার্ভার ক্র্যাশ থেকে বাঁচিয়েছি তা সুন্দরভাবে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"This slide is actually my favorite technical story from the project, because it shows how we solved a real system bottleneck (বটলনেক).

▶ The Problem:
Look at the numbers: each raw TIFF (টিফ) image from the 16K camera is about 20 megabytes (মেগাবাইট). To be honest, if we pushed 20-megabyte images every second through our FastAPI (ফাস্ট-এ-পি-আই) backend or MQTT Broker (এম-কিউ-টি-টি ব্রোকার), our server memory and network would crash in minutes.

▶ Our Solution:
So if you follow this sequence diagram (ডায়াগ্রাম) on the screen, here is the trick we used:
First, the Edge PC (এজ পি-সি) asks FastAPI for a temporary Pre-signed S3 URL (প্রি-সাইনড এস-থ্রি ইউ-আর-এল).
Then, the Edge PC skips our backend completely and uploads that heavy 20-megabyte photo straight to AWS S3 (এ-ডব্লিউ-এস এস-থ্রি).
At the exact same time, the Edge PC sends only a tiny alert message over MQTT (এম-কিউ-টি-টি).
FastAPI just saves the image link in PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) and pings the Next.js (নেক্সট-জে-এস) dashboard via WebSockets (ওয়েব-সকেট).

▶ The Result:
Our backend handles zero heavy files, so even at full factory speed, the server stays fast and never crashes."

--------------------------------------------------------------------------------
SLIDE 08: PRODUCTION INTELLIGENCE & OVERHEAT SOLUTION (লাইভ মনিটরিং ও দুর্ঘটনা রোধ)
[পিলার: How We Solve It & What Actually Happened]
================================================================================
স্লাইডের উদ্দেশ্য:
প্রথমে আমরা কীভাবে প্রবলেমটা সলভ করি তা সহজ ধাপে দেখানো, আর তারপর ফ্যাক্টরিতে বাস্তবে কী ঘটেছিল তা খুব সহজ ইংরেজিতে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Feature three is Production Intelligence (ইন্টেলিজেন্স) — basically (বেসিক্যালি), seeing every machine live so we can stop problems early.

▶ How We Solve the Problem:
Let me show you step by step how we solve machine issues (ইস্যুস) on the floor:
First, every machine sensor (সেন্সর) sends live heat and speed numbers every second through MQTT (এম-কিউ-টি-টি) to our Digital Twin (ডিজিটাল টুইন).
Second, our backend (ব্যাকএন্ড) checks every number against a safe limit on its own.
Third, if any machine gets too hot, the dashboard (ড্যাশবোর্ড) turns red right away and sends an SMS to the shift supervisor (সুপারভাইজার) within 3 seconds.
And fourth, the supervisor opens the chart, sees when the heat started rising, and fixes the machine right there.

▶ What Actually Happened (Real Case):
Now, let me tell you what actually (অ্যাকচুয়ালি) happened on the client's floor:
On Stenter (স্টেন্টার) Line 03, they were running cotton fabric where the safe heat limit is 185 degrees Celsius (সেলসিয়াস). Suddenly, the heat jumped up to 192 degrees.
Before our system, nobody noticed a jump like that until hundreds of meters of cloth got burnt or turned yellow.

▶ The Result:
But this time, AutoTaskX (অটো-টাস্ক-এক্স) caught the 192-degree spike and sent the alert in under 3 seconds. The supervisor lowered the heat right away, and the whole fabric batch (ব্যাচ) was saved with zero waste."

--------------------------------------------------------------------------------
SLIDE 09: TEXTILE OS & DIGITAL TWIN CORE (ভিন্ন ভিন্ন মেশিনকে এক ডিজিটাল টুইনে আনা)
[পিলার: Digital Twin Architecture — Core Focus]
================================================================================
স্লাইডের উদ্দেশ্য:
ইন্ডাস্ট্রি ভিজিটে দেখা পুরোনো ও নতুন সব মেশিনকে কীভাবে একটি ইউনিফাইড Digital Twin-এ আনা হয়েছে তা সহজভাবে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"This slide shows the heart of our Digital Twin (ডিজিটাল টুইন) engine — we call it Textile OS (টেক্সটাইল ও-এস).

▶ What We Saw on the Mill Visit:
When we visited the client's factory, we noticed right away that the machines didn't speak the same language. They had modern (মডার্ন) German stenters (স্টেন্টার), Italian machines, and even 30-year-old controllers (কন্ট্রোলার). Some talked over Modbus (মডবাস), some used Siemens S7 (সিমেন্স এস-সেভেন), and others used OPC-UA (ও-পি-সি ইউ-এ) or RS-485 (আর-এস ফোর-এইটি-ফাইভ). Still, the client wanted every single machine in one Digital Twin.

▶ Our Solution:
So we built Textile OS as a smart translator layer.
Our Edge Gateways (এজ গেটওয়ে) read each machine in its own native language — heat, humidity (হিউমিডিটি), steam pressure, speed, and power usage.
At the edge, we convert all those different signals into one clean, standard JSON (জে-সন) format.
That clean stream updates a live virtual (ভার্চুয়াল) twin for every machine in our backend.

▶ The Result:
Whether a machine is brand new or 30 years old, inside AutoTaskX every machine works as one clean Digital Twin node."

--------------------------------------------------------------------------------
SLIDE 10: IOT DATA TRACE UNDER 25MS (একটি সেন্সর রিডিংয়ের ২৫ মিলিসেকেন্ডের যাত্রা)
[পিলার: Data Pipeline Latency & Performance]
================================================================================
স্লাইডের উদ্দেশ্য:
ইন্টারভিউয়ারকে স্লাইডের বাটনে ক্লিক করে <25ms লাইভ ডাটা ফ্লো দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"You know, the client wanted true real-time updates, so keeping delay ultra-low — what we call latency (লেইটেন্সি) — was huge for us on the backend. Let's trace just one temperature reading right here on Slide 10:

First, inside the Stenter machine, a PT100 (পি-টি হান্ড্রেড) sensor reads 185.5 degrees every 100 milliseconds (মিলিসেকেন্ড).
Next, the IoT Gateway (গেটওয়ে) turns that signal into a tiny MQTT (এম-কিউ-টি-টি) packet.
It travels over the factory network to our FastAPI (ফাস্ট-এ-পি-আই) backend.
AutoTaskX checks the safety limit, updates the Digital Twin, saves it to TimescaleDB (টাইম-স্কেল-ডি-বি), and pushes it to the live screen.

In fact, let's click 'Animate Data Flow' right here on the slide — you can actually (অ্যাকচুয়ালি) watch all six steps finish in under 25 milliseconds (মিলিসেকেন্ড)!"

--------------------------------------------------------------------------------
SLIDE 11: WHY MQTT? DATA TRANSPORT DECISION (এম-কিউ-টি-টি কেন ব্যবহার করলাম?)
[পিলার: MQTT Architecture & Protocol Choice]
================================================================================
স্লাইডের উদ্দেশ্য:
কেন আমরা HTTP-র বদলে MQTT বেছে নিলাম এবং বড় ছবির জন্য কেন সরাসরি S3 ব্যবহার করলাম তা সহজভাবে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Now, you might be wondering — why did we use MQTT (এম-কিউ-টি-টি) instead of normal HTTP REST APIs (রেস্ট এ-পি-আই) for sensor data?

▶ The Problem:
Imagine 50 machines sending readings every second over normal HTTP. HTTP has big headers (হেডার) and opens new connections (কানেকশন) all the time. On weak factory Wi-Fi (ওয়াই-ফাই), that creates a huge bottleneck (বটলনেক) and drops data.

▶ Our Solution:
So we set two simple rules in our system:
Rule one: Tiny sensor readings go through our EMQX MQTT Broker (ই-এম-কিউ-এক্স ব্রোকার). Temperature or speed is only a few bytes, and MQTT uses a super light 2-byte header on a Pub/Sub (পাব/সাব) channel — so our Digital Twin never misses a beat.
Rule two: Heavy 20-megabyte photos NEVER touch MQTT. They go straight over HTTPS (এইচ-টি-টি-পি-এস) to AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) so the broker stays completely free.

▶ The Result:
We get fast, rock-solid communication across the whole factory floor."

--------------------------------------------------------------------------------
SLIDE 12: STORAGE ARCHITECTURE (তিনটি বিশেষায়িত ডেটাবেজ কেন?)
[পিলার: Data Engineering & Polyglot Storage]
================================================================================
স্লাইডের উদ্দেশ্য:
৩টি আলাদা ডেটাবেজ কেন ব্যবহার করা হয়েছে তা খুব সহজ যুক্তিতে বোঝানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"As a Data Engineer, putting every kind of data into one database (ডাটাবেজ) slows things down fast. So we picked three storage tools, each built for one job:

First, PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) for business records — buyer orders, user accounts, machine profiles, and dye recipes where accuracy (অ্যাকিউরেসি) matters most.

Second, TimescaleDB (টাইম-স্কেল-ডি-বি) for time-based sensor data. Since we save millions of sensor rows, a normal table gets really slow over time. TimescaleDB runs inside PostgreSQL using smart time-based tables called Hypertables (হাইপার-টেবলস) — it splits data by time on its own and shrinks storage space by up to 95 percent!

And third, AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) for heavy files — like fabric scan photos and PDF reports.

So when a manager checks a batch history, all three work smoothly side by side."

--------------------------------------------------------------------------------
SLIDE 13: REAL-TIME DELIVERY PIPELINE (লাইভ আপডেট বনাম হিস্টোরিক্যাল রিপোর্ট)
[পিলার: Data Serving & User Experience]
================================================================================
স্লাইডের উদ্দেশ্য:
অপারেটরের লাইভ স্ক্রিন আর ডিরেক্টরের হিস্টোরিক্যাল রিপোর্ট আলাদা চ্যানেলে রাখার কারণ সহজভাবে বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Saving data is half the job — showing it cleanly to different people is just as important.

▶ The Problem:
Floor workers need instant (ইনস্ট্যান্ট) live updates without hitting refresh. Meanwhile, the client's directors (ডিরেক্টর) load heavy charts covering weeks of shift data. If both used the same channel, a big report could freeze the live screen.

▶ Our Solution:
So we split delivery (ডেলিভারি) into two separate lanes:
For live floor screens, FastAPI WebSockets (ওয়েব-সকেট) push Digital Twin changes directly to the Next.js (নেক্সট-জে-এস) dashboard with zero waiting.
For past trends and shift reports, we serve cached REST APIs (রেস্ট এ-পি-আই) powered by TimescaleDB (টাইম-স্কেল-ডি-বি) summaries.

▶ The Result:
Even when a director loads a 30-day energy report, the live machine screen on the floor stays super fast."

--------------------------------------------------------------------------------
SLIDE 14: FEATURE 05 — ERP INTEGRATION (ফ্যাক্টরি থেকে অফিসের ই-আর-পি অটোমেশন)
[পিলার: Enterprise Data Integration]
================================================================================
স্লাইডের উদ্দেশ্য:
ক্লায়েন্টের অফিসের ERP সফটওয়্যারের সাথে ফ্যাক্টরি ফ্লোর কীভাবে অটোমেটিক যুক্ত হলো তা বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Feature five solves a gap the client directly asked for in our very first office meeting — connecting the factory floor with their head-office ERP (ই-আর-পি) software.

▶ The Problem:
Like most big textile groups, the client already uses an ERP like SAP (এস-এ-পি), Datatex NOW (ডাটাটেক্স নাউ), or Infor M3 (ইনফর এম-থ্রি). Before AutoTaskX, staff wrote production numbers on paper, and someone typed them into the ERP one or two days later — often making mistakes.

▶ Our Solution:
So we built a two-way ERP bridge:
Work orders flow down from the ERP straight into AutoTaskX as digital jobs.
And when a dyeing or inspection batch finishes, actual meters made and exact chemicals used sync right back up into the ERP stock records.

▶ The Result:
Zero two-day delays, zero manual typing errors, and 100 percent clear stock tracking for the client."

--------------------------------------------------------------------------------
SLIDE 15: COMPLETE 4-ZONE ARCHITECTURE (পুরো সিস্টেমের ৪-জোন ব্লুপ্রিন্ট)
[পিলার: System Architecture & Scalability]
================================================================================
স্লাইডের উদ্দেশ্য:
৪টি জোনে পুরো আর্কিটেকচার ব্লুপ্রিন্ট এক নজরে দেখানো এবং এটি কত সহজে স্কেল করা যায় তা বলা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"If you look at this slide, this is our full architecture (আর্কিটেকচার) blueprint (ব্লুপ্রিন্ট) in four clear zones:

Zone one is the Physical Factory — stenters, dyeing machines, looms (লুমস), cameras, and over 100 sensors.
Zone two is the Connection Layer — Edge Gateways (এজ গেটওয়ে) reading Modbus (মডবাস) or OPC-UA (ও-পি-সি ইউ-এ), linked to our EMQX MQTT Broker (ই-এম-কিউ-এক্স ব্রোকার).
Zone three is the Core & Storage Layer — our FastAPI (ফাস্ট-এ-পি-আই) backend, AI vision models, Digital Twin (ডিজিটাল টুইন) state, and our three databases: PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল), TimescaleDB (টাইম-স্কেল-ডি-বি), and AWS S3 (এ-ডব্লিউ-এস এস-থ্রি).
Zone four is Delivery & Business Apps — the Next.js (নেক্সট-জে-এস) dashboard (ড্যাশবোর্ড), mobile app, SMS alerts, and the ERP (ই-আর-পি) bridge.

And you know, the client wanted to make sure they could grow later. Because each layer is cleanly separated, if they add 50 more machines in another building tomorrow, we just add gateways in Zones one and two — zero core code changes needed."

--------------------------------------------------------------------------------
SLIDE 16: MEASURABLE BUSINESS OUTCOMES (গাজীপুর মিলে বাস্তব ফলাফল ও আরওআই)
[পিলার: Outcomes & Business ROI]
================================================================================
স্লাইডের উদ্দেশ্য:
গাজীপুর টেক্সটাইল মিলে পাওয়া বাস্তব ও সন্তোষজনক ফলাফলগুলো দেখানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"At the end of the day, great engineering should deliver real business wins. On this slide, you're seeing live numbers from the client's Gazipur (গাজীপুর) Textile Mill number four:

Out of 26 connected machines, 24 are running non-stop right now, and 2 are offline for planned maintenance (মেইনটেন্যান্স) — so nothing is hidden anymore.
Stenter heat is steady at 185.5 degrees with zero critical alerts.
In one day, we tracked 42,500 meters of fabric in real time.
With AI vision inspection, the Right-First-Time (রাইট-ফার্স্ট-টাইম) quality pass rate hit 99.2 percent.
And overall machine efficiency (এফিশিয়েন্সি) — known as OEE (ও-ই-ই) — jumped by 14 percent in just four months.

Now the client can simply open a tablet from anywhere in the world and see how their whole factory is running."

--------------------------------------------------------------------------------
SLIDE 17: AI AUTOMATION & FUTURE ROADMAP (এ-আই অটোমেশন ও ভবিষ্যৎ পরিকল্পনা)
[পিলার: AI Automation & Future Scalability]
================================================================================
স্লাইডের উদ্দেশ্য:
ভবিষ্যতের AI Automation ও Predictive Maintenance পরিকল্পনা সহজ ও স্মার্টভাবে তুলে ধরা।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"Because those first four months went so well, we also planned a five-step future roadmap (রোডম্যাপ) with the client to bring in even smarter AI automation (এ-আই অটোমেশন):

Step one is Connect More — bringing the rest of the factory machines into the same Digital Twin (ডিজিটাল টুইন), so the client gets 100 percent live coverage (কভারেজ).
Step two is Full Auto Inspection (ইন্সপেকশন) — where cameras check every meter of fabric on their own, so workers don't need to click photos manually (ম্যানুয়ালি).
Step three is Smart Past Data — using months of TimescaleDB (টাইম-স্কেল-ডি-বি) data to predict (প্রিডিক্ট) how dyes behave in winter or summer.
Step four is Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স) — watching motor vibration (ভাইব্রেশন) and extra heat, so AI warns the team before any machine breaks down.
And step five is Closed-Loop Control (ক্লোজড-লুপ কন্ট্রোল) — where the Digital Twin (ডিজিটাল টুইন) itself safely sends small speed or heat updates straight back to the machine PLC (পি-এল-সি) on its own."

--------------------------------------------------------------------------------
SLIDE 18: CONCLUSION & Q&A (সমাপ্তি ও প্রশ্নোত্তর পর্ব)
[পিলার: Closing Statement]
================================================================================
স্লাইডের উদ্দেশ্য:
আত্মবিশ্বাসের সাথে প্রজেক্টের মূল কথা শেষ করে ইন্টারভিউয়ারকে প্রশ্নের জন্য আমন্ত্রণ জানানো।

[কীভাবে বলবেন — স্পোকেন স্ক্রিপ্ট]:
"So to wrap things up, AutoTaskX (অটো-টাস্ক-এক্স) isn't just a demo or theory. It started when a prominent (প্রমিনেন্ট) Bangladeshi textile client walked into our office asking for full automation (অটোমেশন) and a live Digital Twin (ডিজিটাল টুইন). After visiting their factory, gathering the requirements, and drawing the software blueprint (ব্লুপ্রিন্ট), our three-developer core team built both the backend and frontend in four months — and as one of the main backend engineers doing around 40 to 50 percent of the work, seeing it run 24/7 on a real factory floor feels awesome.

By mixing clean Data Engineering, fast MQTT streaming, live Digital Twin updates, and practical (প্র্যাকটিক্যাল) AI automation, we turned disconnected (ডিসকানেক্টেড) machines into one connected smart mill.

Thank you so much for listening! I'd be really happy to answer any questions you have about our backend architecture (আর্কিটেকচার), Digital Twin (ডিজিটাল টুইন) setup, MQTT (এম-কিউ-টি-টি) flow, or AI pipeline (পাইপলাইন) — feel free to ask anything."

================================================================================
MASTER CHEAT SHEET: ৬টি গুরুত্বপূর্ণ ইন্টারভিউ প্রশ্ন ও সহজ, ফ্লুয়েন্ট উত্তর
================================================================================

প্রশ্ন ১: "How do you keep the Digital Twin (ডিজিটাল টুইন) always in sync with the physical machines?"
স্মার্ট উত্তর:
"You know, every machine has an Edge Gateway (এজ গেটওয়ে) reading sensors every 100 milliseconds (মিলিসেকেন্ড). It converts (কনভার্টস) the reading into clean JSON (জে-সন) and sends it over MQTT (এম-কিউ-টি-টি) to our EMQX Broker (ই-এম-কিউ-এক্স ব্রোকার). Our FastAPI (ফাস্ট-এ-পি-আই) backend picks it up right away, updates the Digital Twin in memory, saves history to TimescaleDB (টাইম-স্কেল-ডি-বি), and pushes live updates to the dashboard (ড্যাশবোর্ড) via WebSockets (ওয়েব-সকেট) — all in under 25 milliseconds (মিলিসেকেন্ড)."

প্রশ্ন ২: "Why did you pick MQTT (এম-কিউ-টি-টি) instead of regular HTTP APIs (এইচ-টি-টি-পি এ-পি-আই) for sensor data?"
স্মার্ট উত্তর:
"To be honest, HTTP (এইচ-টি-টি-পি) is great for normal web pages, but when sensors send data every second, HTTP headers (হেডার) are too heavy and slow things down — creating a bottleneck (বটলনেক) on factory Wi-Fi. MQTT (এম-কিউ-টি-টি) only uses a tiny 2-byte header over an always-open connection. Plus, with QoS Level 1 (কিউ-ও-এস লেভেল ওয়ান), even if Wi-Fi flickers for a moment, we don't drop important machine readings."

প্রশ্ন ৩: "Why TimescaleDB (টাইম-স্কেল-ডি-বি)? Why not just plain PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) or MongoDB (মঙ্গো-ডি-বি)?"
স্মার্ট উত্তর:
"Actually (অ্যাকচুয়ালি), we needed both worlds for the client. Orders and dye recipes need clean relational (রিলেশনাল) tables, so PostgreSQL (পোস্ট-গ্রে-এস-কিউ-এল) gives us rock-solid accuracy (অ্যাকিউরেসি). But putting millions of sensor rows in a regular table makes searches slow over time. Because TimescaleDB (টাইম-স্কেল-ডি-বি) runs right inside PostgreSQL using time-based Hypertables (হাইপার-টেবলস), it splits data by time on its own and saves up to 95 percent disk space — all in one database system."

প্রশ্ন ৪: "What happens if the factory internet drops while uploading a 20MB inspection (ইন্সপেকশন) image?"
স্মার্ট উত্তর:
"That's a real issue we saw during our mill visit, so we handled it right at the edge. On the Edge PC (এজ পি-সি), we built a local FIFO disk queue (ফিফো ডিস্ক কিউ). Every photo saves to the local disk first, and we never delete it until AWS S3 (এ-ডব্লিউ-এস এস-থ্রি) confirms a successful upload. Once internet is back, waiting photos upload in exact order — zero lost frames."

প্রশ্ন ৫: "Why did you choose FastAPI (ফাস্ট-এ-পি-আই) over Django (জ্যাঙ্গো) for the backend?"
স্মার্ট উত্তর:
"Basically (বেসিক্যালি), we had hundreds of live IoT streams and WebSocket (ওয়েব-সকেট) dashboards (ড্যাশবোর্ডস) running at the same time. Django (জ্যাঙ্গো) is mostly built for traditional (ট্র্যাডিশনাল) one-by-one web requests and feels heavier for non-stop streaming. FastAPI (ফাস্ট-এ-পি-আই) has native async support (AsyncIO / অ্যাসিঙ্ক-আই-ও), so it handles many live MQTT (এম-কিউ-টি-টি) and WebSocket connections at once using much less CPU (সি-পি-ইউ) and memory."

প্রশ্ন ৬: "How is AI automation (এ-আই অটোমেশন) actually helping here instead of just being a buzzword (বাজওয়ার্ড)?"
স্মার্ট উত্তর:
"To be honest, the client didn't want AI just for show — they wanted real business results. So we used it in three practical (প্র্যাকটিক্যাল) ways: first, OpenCV (ওপেন-সি-ভি) and YOLO (ইয়োলো) catching tiny <0.5mm fabric flaws at 120 meters per minute; second, smart heat alerts that stopped fabric from burning at 192 degrees; and third, storing clean historical (হিস্টোরিক্যাল) data in TimescaleDB (টাইম-স্কেল-ডি-বি) so we can spot motor vibration (ভাইব্রেশন) issues early with Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স)."

================================================================================
[End of Guide — Smile, stay relaxed, and walk them through it step by step!]
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
        {"label": "Key Challenge", "val": "20MB Raw TIFF Frames Crashing API / MQTT"},
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
        {"label": "Why EMQX MQTT", "val": "Always-Open Connection, Low Bandwidth, Zero Drop QoS"},
        {"label": "Why Direct S3", "val": "Keeps 20MB Vision Blobs Out of MQTT Broker Memory"},
        {"label": "Digital Twin Feed", "val": "High-Frequency Pub/Sub Streams Update Twin State Live"}
    ],
    "12": [
        {"label": "Storage Strategy", "val": "Three Specialized Databases Matched to Workload"},
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
        {"label": "Audit Impact", "val": "100% Paperless & Clear Stock Tracking"}
    ],
    "15": [
        {"label": "Zone 1 & Zone 2", "val": "100+ Floor Sensors -> Edge Gateways -> EMQX MQTT"},
        {"label": "Zone 3 (Core)", "val": "FastAPI, AI Models, Digital Twin & 3 Databases"},
        {"label": "Zone 4 (Apps)", "val": "Next.js Dashboard, Mobile QA, SMS & ERP Connector"},
        {"label": "Client Expansion", "val": "Cleanly Separated — Add 50 Machines Without Code Rewrites"}
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
        {"label": "Core Pillars", "val": "Digital Twin · EMQX MQTT · Data Pipeline · AI Vision"},
        {"label": "Q&A Readiness", "val": "Ready for Architecture, Pipeline & Data Deep Dive"}
    ]
}

cheat_marker = 'MASTER CHEAT SHEET: ৬টি গুরুত্বপূর্ণ ইন্টারভিউ প্রশ্ন ও সহজ, ফ্লুয়েন্ট উত্তর'
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

# Pure Bangla presentation guide dataset for /guide/bd (guide-bd.html)
# Mirrors the exact current 18-slide structure, client engagement story, 3-dev core team (~40-50% backend),
# solution-first Slide 08, and 6 interview Q&As in natural, confident spoken Bangladeshi Bangla.
bangla_slides = [
    {
        "num": "01",
        "en_title": "PROJECT OVERVIEW & CLIENT VISION",
        "bn_title": "প্রজেক্ট পরিচিতি ও ক্লায়েন্টের ভিশন",
        "pillar": "১. ক্লায়েন্ট ভিশন ও ওভারভিউ",
        "objective": "আগে থেকেই নিজের পরিচয় দেওয়া থাকায় সরাসরি ক্লায়েন্ট প্রজেক্ট দিয়ে শুরু করা — ক্লায়েন্ট অফিসে এসে কী চেয়েছিলেন, ফ্যাক্টরি ভিজিটের পর আমরা কী ব্লুপ্রিন্ট বানাই এবং ৩ জনের কোর টিমে আপনার ৪০–৫০% ব্যাকএন্ড অবদান সহজ ও সাবলীল বাংলায় তুলে ধরা।",
        "speech": (
            "চলুন সরাসরি প্রজেক্টে চলে যাই — আমাদের প্ল্যাটফর্মের নাম AutoTaskX। সহজ কথায় বললে, এটি বাংলাদেশের টেক্সটাইল ইন্ডাস্ট্রির একটি বড় ও শীর্ষস্থানীয় কোম্পানির জন্য তৈরি রিয়েল-টাইম Industrial IoT এবং Digital Twin প্ল্যাটফর্ম।\n\n"
            "▶ কীভাবে শুরু হয়েছিল (ক্লায়েন্টের রিকোয়েস্ট):\n"
            "সত্যি বলতে, এই প্রজেক্টের শুরুটা ছিল বেশ ইন্টারেস্টিং। ক্লায়েন্ট নিজেরাই বুঝতে পেরেছিলেন যে তাদের ফ্যাক্টরিতে বড় কিছু গ্যাপ আছে, তাই তারা সরাসরি আমাদের অফিসে আসেন। তারা পুরো ফ্যাক্টরিতে পূর্ণ অটোমেশন চেয়েছিলেন — যেন পুরো ফ্যাক্টরি ফ্লোরটাকে একটি লাইভ Digital Twin-এ রূপান্তর করা যায়।\n\n"
            "▶ ফ্যাক্টরি ভিজিট ও টিমের কাজ:\n"
            "ওই মিটিংয়ের পরপরই আমরা তাদের ফ্যাক্টরি ভিজিট করি এবং বাস্তবের মেশিনগুলো — যেমন dyeing jets, stenters এবং color lab ঘুরে দেখি। সেখান থেকে সব রিকোয়ারমেন্টস তালিকা করে আমরা একটি পরিষ্কার সফটওয়্যার ব্লুপ্রিন্ট তৈরি করি। টানা চার মাসে আমাদের তিনজন ডেভেলপারের কোর টিম মিলে পুরো ব্যাকএন্ড এবং ফ্রন্টএন্ড তৈরি করে। মূল ব্যাকএন্ড ইঞ্জিনিয়ারদের একজন হিসেবে মোট কাজের প্রায় ৪০ থেকে ৫০ শতাংশ আমি নিজে করেছি — বিশেষ করে MQTT Data Pipeline, Digital Twin লাইভ আপডেট এবং AI Automation-এর কাজগুলো। আর একজন ব্যাকএন্ড ও IoT অনুরাগী হিসেবে বাস্তব ফ্যাক্টরির হার্ডওয়্যারের সাথে কাজ করাটা আমার জন্য দারুণ অভিজ্ঞতা ছিল।\n\n"
            "▶ ফলাফল:\n"
            "স্লাইডের ডান পাশে আপনারা আমাদের লাইভ Digital Twin স্ক্রিন দেখতে পাচ্ছেন। প্রতিটি মেশিনের ডেটা ২৫ মিলিসেকেন্ডেরও কম সময়ে আপডেট হয় এবং সিস্টেমটি আজও ২৪/৭ লাইভ প্রোডাকশনে চলছে।"
        ),
        "tech_points": [
            {"label": "ক্লায়েন্ট প্রোফাইল", "val": "বাংলাদেশের শীর্ষস্থানীয় টেক্সটাইল ইন্ডাস্ট্রি লিডার"},
            {"label": "টিম ও ভূমিকা", "val": "৩-জনের কোর টিম · মূল ব্যাকএন্ড ইঞ্জিনিয়ার (~৪০–৫০%)"},
            {"label": "কাজের ধাপ", "val": "অফিস মিটিং → ফ্যাক্টরি ভিজিট → সফটওয়্যার ব্লুপ্রিন্ট"},
            {"label": "প্রোডাকশন প্রমাণ", "val": "৪ মাসে তৈরি · ২৪/৭ লাইভ প্রোডাকশন (<25ms HUD)"}
        ]
    },
    {
        "num": "02",
        "en_title": "CLIENT PAIN POINTS & MILL REALITY",
        "bn_title": "ক্লায়েন্টের সমস্যা ও ফ্যাক্টরি ভিজিটের অভিজ্ঞতা",
        "pillar": "১. ক্লায়েন্টের সমস্যা ও ভিজিট",
        "objective": "ক্লায়েন্ট অফিসে এসে কী কী সমস্যার কথা বলেছিলেন এবং ফ্যাক্টরি ভিজিটে গিয়ে আমরা কী কী বটলনেক দেখেছি তা সহজ গল্পের মতো বলা।",
        "speech": (
            "ক্লায়েন্ট যখন প্রথম আমাদের অফিসে আসেন, তখন তারা প্রতিদিনের কাজ ধীর করে দেওয়া বাস্তব সমস্যাগুলোর কথা আমাদের জানান। এরপর ফ্যাক্টরি ভিজিটে গিয়ে আমরা ফ্লোরে এই ৪টি বড় বটলনেক সরাসরি দেখতে পাই:\n\n"
            "প্রথমত, অতিরিক্ত ম্যানুয়াল কাজ। ল্যাবের স্টাফরা হাতে-কলমে রঙের হিসাব করতেন, আর সুপারভাইজাররা কাগজের খাতায় মেশিনের রিডিং লিখে রাখতেন। এতে অনেক সময় নষ্ট হতো এবং মানুষের ভুল হওয়ার ঝুঁকি থাকত।\n\n"
            "দ্বিতীয়ত, মেশিনগুলোর মধ্যে কোনো সংযোগ ছিল না। প্রতিটি মেশিন আলাদা দ্বীপের মতো কাজ করত। একটি মেশিন অতিরিক্ত গরম হয়ে গেলেও অন্য কেউ তা সাথে সাথে জানতে পারত না।\n\n"
            "তৃতীয়ত, ম্যানেজমেন্টের হাতে কোনো লাইভ ডেটা ছিল না। ক্লায়েন্ট চাইতেন লাইভ আপডেট দেখতে, কিন্তু তখন তারা কেবল শিফট শেষে অথবা সপ্তাহে একবার রিপোর্ট পেতেন।\n\n"
            "আর চতুর্থত, দেরিতে ব্যবস্থা নেওয়ায় বড় আর্থিক ক্ষতি হতো। কেউ রঙের অমিল বা কাপড় পুড়ে যাওয়া ধরতে ধরতেই পুরো ১০,০০০ মিটারের একটি ব্যাচ নষ্ট হয়ে যেত।\n\n"
            "▶ ক্লায়েন্ট যা চেয়েছিলেন:\n"
            "তাই ক্লায়েন্ট আমাদের পরিষ্কারভাবে বলেন — এই আন্দাজ-নির্ভর কাজ বন্ধ করে পুরো ফ্যাক্টরির জন্য একটি লাইভ ও অটোমেটেড Digital Twin তৈরি করে দিতে।"
        ),
        "tech_points": [
            {"label": "ক্লায়েন্টের সমস্যা", "val": "খাতা-কলমের ম্যানুয়াল লগ ও বিচ্ছিন্ন মেশিন"},
            {"label": "ফ্যাক্টরি ভিজিট অডিট", "val": "পুরোনো মেশিনারি ও শিফট-শেষের ব্লাইন্ডস্পট শনাক্ত"},
            {"label": "ব্যবসায়িক ঝুঁকি", "val": "একবারে ১০,০০০ মিটার পর্যন্ত কাপড়ের ব্যাচ বাতিল"},
            {"label": "মূল লক্ষ্য", "val": "অটোমেটেড ডেটা-ড্রিভেন Digital Twin ভিজিবিলিটি"}
        ]
    },
    {
        "num": "03",
        "en_title": "ARCHITECTURE BLUEPRINT & 5 MODULES",
        "bn_title": "সফটওয়্যার ব্লুপ্রিন্ট ও পাঁচটি মডিউল",
        "pillar": "২. আর্কিটেকচার ব্লুপ্রিন্ট",
        "objective": "সফটওয়্যার ব্লুপ্রিন্টে থাকা ৫টি মডিউল সহজ ও সাবলীল ভাষায় ইন্টারভিউয়ারকে দেখানো।",
        "speech": (
            "ফ্যাক্টরি ভিজিটের পর আমরা এমন একটি পরিষ্কার সফটওয়্যার ব্লুপ্রিন্ট তৈরি করি, যাতে ক্লায়েন্টকে নতুন কোনো মেশিন কিনতে না হয়। বরং একটি শেয়ার্ড Data Pipeline-এর ওপর ভিত্তি করে আমরা AutoTaskX-কে পাঁচটি কানেক্টেড মডিউলে সাজাই। চলুন স্লাইডে মডিউলগুলো দেখে নিই:\n\n"
            "এক নম্বর হলো Color Formulation — যা ল্যাবের ম্যানুয়াল ট্রায়াল-অ্যান্ড-এরর বাদ দিয়ে দ্রুত নির্ভুল ম্যাথের মাধ্যমে রঙের রেসিপি দেয়।\n"
            "দুই নম্বর হলো Visual Quality Inspection — যেখানে ক্যামেরা এবং AI Automation ব্যবহার করে সাথে সাথে কাপড়ের ডিফেক্ট ধরা হয়।\n"
            "তিন নম্বর হলো Production Intelligence — যা মেশিনের রানটাইম, এফিশিয়েন্সি এবং হঠাৎ তাপমাত্রা বেড়ে যাওয়া নজরদারি করে।\n"
            "চার নম্বর হলো Textile OS & Digital Twin — যা বাস্তব সেন্সর ও PLC-র সাথে যুক্ত হয়ে প্রতিটি মেশিনের একটি লাইভ ডিজিটাল কপি বজায় রাখে।\n"
            "আর পাঁচ নম্বর হলো ERP Integration — যা ফ্যাক্টরির উৎপাদনের হিসাব সরাসরি SAP বা Datatex-এ পাঠিয়ে দেয়।\n\n"
            "এতে প্রতিটি টিম নিজের কাজের জন্য সহজ একটি ড্যাশবোর্ড পায়, আর পেছনে পাঁচটি মডিউলই একসাথে সিঙ্ক হয়ে কাজ করে।"
        ),
        "tech_points": [
            {"label": "সমাধান ব্লুপ্রিন্ট", "val": "একটি শেয়ার্ড Data Pipeline-এ ৫টি মডিউলার ইঞ্জিন"},
            {"label": "মেশিন বদল নয়", "val": "বিদ্যমান Dyeing, Stenter ও ল্যাব মেশিনেই যুক্ত"},
            {"label": "ইন্টিগ্রেশন মডেল", "val": "EMQX Broker-এর মাধ্যমে ইভেন্ট-ড্রিভেন MQTT Pub/Sub"},
            {"label": "AI অটোমেশন", "val": "স্বয়ংক্রিয় ডাই ম্যাথ, ডিফেক্ট ডিটেকশন ও অ্যালার্ট"}
        ]
    },
    {
        "num": "04",
        "en_title": "END-TO-END DATA PIPELINE",
        "bn_title": "সেন্সর থেকে ড্যাশবোর্ডে ডেটা যাত্রা",
        "pillar": "২. ডেটা পাইপলাইন ও MQTT",
        "objective": "একজন Data Engineer হিসেবে ৪ ধাপের ডেটা ফ্লো (Sense → Connect → Process → Deliver) খুব সহজ করে বোঝানো।",
        "speech": (
            "স্লাইডের এই চারটি ধাপের দিকে তাকালে দেখবেন, এটাই আমাদের মূল Data Pipeline — অর্থাৎ Digital Twin-এর হৃদপিণ্ড। চলুন একসাথে ধাপগুলো দেখি:\n\n"
            "ধাপ এক হলো Sense। ক্লায়েন্টের মেশিনে লাগানো সেন্সর এবং হাই-স্পিড ক্যামেরা তাপমাত্রা, গতি এবং কাপড়ের ছবি সংগ্রহ করে।\n\n"
            "ধাপ দুই হলো Connect। আমাদের Edge Gateway সেই কাঁচা সিগন্যালকে পরিষ্কার JSON ফরম্যাটে রূপান্তর করে MQTT-র মাধ্যমে EMQX Broker-এ পাঠায়।\n\n"
            "ধাপ তিন হলো Process। আমাদের FastAPI ব্যাকএন্ড সেই MQTT স্ট্রিম গ্রহণ করে, ডেটা যাচাই করে, Digital Twin স্টেট আপডেট করে এবং ইতিহাস হিসেবে TimescaleDB-তে সেভ করে।\n\n"
            "ধাপ চার হলো Deliver। WebSockets-এর মাধ্যমে লাইভ আপডেট সরাসরি আমাদের Next.js স্ক্রিনে চলে আসে।\n\n"
            "সত্যি বলতে, ফ্লোরে একটি মেশিনের তাপমাত্রা পরিবর্তন হওয়া থেকে শুরু করে ক্লায়েন্টের স্ক্রিনে দেখা যাওয়া পর্যন্ত পুরো যাত্রাটি ২৫ মিলিসেকেন্ডেরও কম সময়ে সম্পন্ন হয়।"
        ),
        "tech_points": [
            {"label": "ধাপ ১ (Sense)", "val": "PT100 RTD সেন্সর ও Basler CoaXPress 16K ক্যামেরা"},
            {"label": "ধাপ ২ (Connect)", "val": "Edge Gateway -> Normalized JSON -> EMQX MQTT Broker"},
            {"label": "ধাপ ৩ (Process)", "val": "FastAPI Async Engine -> Digital Twin + TimescaleDB"},
            {"label": "ধাপ ৪ (Deliver)", "val": "WebSocket-এ Next.js UI-তে লাইভ পুশ (<25ms E2E)"}
        ]
    },
    {
        "num": "05",
        "en_title": "FEATURE 01 — COLOR FORMULATION",
        "bn_title": "স্মার্ট কালার ফর্মুলেশন",
        "pillar": "৩. ল্যাব অটোমেশন",
        "objective": "ক্লায়েন্টের ডাইং ল্যাবের রঙ মেলানোর সমস্যা কীভাবে ম্যাথ ও অটোমেশন দিয়ে সমাধান হলো তা বলা।",
        "speech": (
            "চলুন এক নম্বর ফিচার দেখি — Color Formulation।\n\n"
            "▶ ক্লায়েন্টের সমস্যা:\n"
            "আমরা যখন ক্লায়েন্টের ডাই ল্যাব ভিজিট করি, তখন দেখি প্রথম চেষ্টাতেই বায়ারের রঙের স্যাম্পল মেলানোটা ছিল সবচেয়ে বড় বটলনেক। ল্যাবের কেমিস্টদের হাতে মিশিয়ে টেস্ট ব্যাচ বানাতে ৫ থেকে ৬ ঘণ্টা সময় লাগত, এবং প্রচুর রঙ ও পানি নষ্ট হতো। ক্লায়েন্ট এই ধাপটি অটোমেট করতে চেয়েছিলেন।\n\n"
            "▶ আমাদের সমাধান:\n"
            "তাই আমরা Kubelka-Munk (কুবেলকা-মাঙ্ক) কালার ম্যাথ ব্যবহার করে একটি স্মার্ট রেসিপি ইঞ্জিন তৈরি করি। প্রথমে একটি রঙ মাপার যন্ত্র — Spectrophotometer (স্পেকট্রোফোটোমিটার) — টার্গেট কাপড়টি স্ক্যান করে। এরপর আমাদের ইঞ্জিন প্রতি ১০০ কেজি কাপড়ের জন্য ঠিক কত গ্রাম ডাই লাগবে তা হিসাব করে সরাসরি auto-dispenser-এ পাঠিয়ে দেয়। আর নিরাপত্তার জন্য ল্যাবে বড় ব্যাচ ডাইংয়ের আগে ছোট একটি beaker (বিকার) চেক করা হয়।\n\n"
            "▶ ফলাফল:\n"
            "রঙের পার্থক্য — যাকে Delta-E (ডেল্টা-ই) বলে — ১.০-এর নিচে থাকে, যা মানুষের চোখে একদম নিখুঁত ম্যাচ, এবং প্রথম চেষ্টাতেই ল্যাবে সঠিক রঙ পাওয়ার হার ৮৫ শতাংশ ছাড়িয়ে গেছে।"
        ),
        "tech_points": [
            {"label": "ল্যাবের প্রয়োজন", "val": "৫–৬ ঘণ্টার ম্যানুয়াল ডাই ট্রায়াল-অ্যান্ড-এরর কমানো"},
            {"label": "সমাধান ইঞ্জিন", "val": "Kubelka-Munk স্পেকট্রাল ম্যাথ + অটো রেসিপি"},
            {"label": "রঙের সূক্ষ্মতা", "val": "CIE ΔE < 1.0 (৮৫%+ প্রথম চেষ্টায় ম্যাচ, ল্যাব ভ্যালিডেটেড)"},
            {"label": "ডিস্পেন্সারি সিঙ্ক", "val": "প্রতি ১০০ কেজির নিখুঁত গ্রাম হিসাব Auto-Dispenser-এ"}
        ]
    },
    {
        "num": "06",
        "en_title": "FEATURE 02 — AI VISION INSPECTION",
        "bn_title": "এ-আই ভিত্তিক কাপড়ের মান পরীক্ষা",
        "pillar": "৩. AI ভিশন অটোমেশন",
        "objective": "ক্লায়েন্টের ফ্লোরে কাপড়ের ডিফেক্ট ধরতে AI Automation কীভাবে কাজ করে তা সহজ ও সাবলীলভাবে বলা।",
        "speech": (
            "এবার দুই নম্বর ফিচার দেখুন — AI Automation ব্যবহার করে Visual Quality Inspection।\n\n"
            "▶ ক্লায়েন্ট যা চেয়েছিলেন:\n"
            "চিন্তা করে দেখুন — যখন মেশিনের ভেতর দিয়ে মিনিটে ৮০ থেকে ১২০ মিটার গতিতে কাপড় ছোটে, তখন মানুষের চোখ দিয়ে আধা মিলিমিটারেরও ছোট সুতা কাটা বা তেলের দাগ ধরা অসম্ভব। তাছাড়া কর্মীরা ব্যক্তিগত ফোনে ছবি তুলে রাখতেন এবং সেগুলো হারিয়ে যেত। ক্লায়েন্ট চেয়েছিলেন প্রতিটি মিটার কাপড় অটোমেটিক ও ডিজিটালভাবে চেক করার ব্যবস্থা।\n\n"
            "▶ আমাদের সমাধান:\n"
            "তাই আমরা একটি AI ভিশন মডেলের সাথে দুটি ক্যামেরা সোর্স যুক্ত করি:\n"
            "প্রথমত, কাপড়ের লাইনের ঠিক ওপরে বসানো দ্রুতগতির Basler (বাসলার) 16K line-scan camera।\n"
            "এবং দ্বিতীয়ত, ফ্লোরের চেকারদের দ্রুত স্পট-চেকের ছবি তোলার জন্য একটি মোবাইল অ্যাপ।\n\n"
            "ছবিগুলো আসার সাথে সাথে OpenCV কাপড়ের স্ট্রিপটি প্রস্তুত করে, আর আমাদের YOLO AI মডেল ০.৫ মিলিমিটারের চেয়ে ছোট যেকোনো ত্রুটির চারপাশে বক্স এঁকে দেয় এবং কী ধরনের ডিফেক্ট তা ট্যাগ করে।\n\n"
            "▶ ফলাফল:\n"
            "এখন প্রতিটি মিটার কাপড় স্বয়ংক্রিয়ভাবে পরীক্ষা হয় এবং পরিষ্কার একটি ডিজিটাল রিপোর্ট তৈরি হয় — কোনো অনুমানের সুযোগ নেই।"
        ),
        "tech_points": [
            {"label": "কোয়ালিটি চাহিদা", "val": "৮০–১২০ মি./মিনিট গতিতে <0.5mm ত্রুটি স্বয়ংক্রিয় ধরা"},
            {"label": "হার্ডওয়্যার ইনপুট", "val": "Basler racer 2L (16K Line-Scan) + ফ্লোর মোবাইল অ্যাপ"},
            {"label": "AI অটোমেশন", "val": "OpenCV ইমেজ স্টিচিং + YOLO ডিফেক্ট ক্লাসিফিকেশন"},
            {"label": "অডিট ট্রেইল", "val": "তাৎক্ষণিক বাউন্ডিং বক্স ও অটো রোল ডিফেক্ট রিপোর্ট"}
        ]
    },
    {
        "num": "07",
        "en_title": "KEY CHALLENGE & SOLUTION — IMAGE & DATA OFFLOADING",
        "bn_title": "বড় ছবি বনাম সার্ভার স্পিড",
        "pillar": "৪. চ্যালেঞ্জ ও ডেটা অফলোড",
        "objective": "২০ মেগাবাইটের ভারী ছবি আর ছোট সেন্সর ডেটা আলাদা রেখে আমরা কীভাবে সার্ভার ক্র্যাশ থেকে বাঁচিয়েছি তা সুন্দরভাবে বলা।",
        "speech": (
            "সত্যি বলতে, এই স্লাইডটি আমার প্রজেক্টের সবচেয়ে প্রিয় টেকনিক্যাল গল্প — কারণ এখানে আমরা বাস্তব সিস্টেমের বড় একটি বটলনেক সমাধান করেছি।\n\n"
            "▶ সমস্যা:\n"
            "সংখ্যাগুলো দেখুন: 16K ক্যামেরা থেকে আসা প্রতিটি র TIFF (টিফ) ছবির সাইজ প্রায় ২০ মেগাবাইট। প্রতি সেকেন্ডে যদি ২০ মেগাবাইটের ছবি আমরা FastAPI ব্যাকএন্ড বা MQTT Broker-এর ভেতর দিয়ে পাঠাতাম, তাহলে কয়েক মিনিটের মধ্যেই সার্ভারের মেমোরি ও নেটওয়ার্ক ক্র্যাশ করত।\n\n"
            "▶ আমাদের সমাধান:\n"
            "স্ক্রিনের এই সিকোয়েন্স ডায়াগ্রামটি অনুসরণ করলে দেখবেন আমরা কী কৌশল ব্যবহার করেছি:\n"
            "প্রথমে Edge PC আমাদের FastAPI থেকে একটি অস্থায়ী Pre-signed S3 URL (প্রি-সাইনড এস-থ্রি ইউ-আর-এল) চায়।\n"
            "এরপর Edge PC আমাদের ব্যাকএন্ডকে পুরোপুরি বাইপাস করে ২০ মেগাবাইটের ভারী ছবিটি সরাসরি AWS S3-তে আপলোড করে দেয়।\n"
            "ঠিক একই সময়ে Edge PC শুধুমাত্র ছোট্ট একটি অ্যালার্ট মেসেজ MQTT-র মাধ্যমে পাঠায়।\n"
            "FastAPI কেবল ছবির লিংকটি PostgreSQL-এ সেভ করে এবং WebSockets দিয়ে Next.js ড্যাশবোর্ডে জানিয়ে দেয়।\n\n"
            "▶ ফলাফল:\n"
            "আমাদের ব্যাকএন্ডে কোনো ভারী ফাইল লোড পড়ে না, তাই ফ্যাক্টরি সর্বোচ্চ গতিতে চললেও সার্ভার ফাস্ট থাকে এবং কখনো ক্র্যাশ করে না।"
        ),
        "tech_points": [
            {"label": "মূল চ্যালেঞ্জ", "val": "২০MB র TIFF ছবিতে API / MQTT ক্র্যাশের ঝুঁকি"},
            {"label": "ব্লুপ্রিন্ট সমাধান", "val": "Edge PC থেকে প্যারালাল Pre-signed AWS S3 ডিরেক্ট আপলোড"},
            {"label": "MQTT পৃথকীকরণ", "val": "MQTT-তে কেবল হালকা মেটাডাটা ও ডিফেক্ট অ্যালার্ট"},
            {"label": "স্থায়িত্ব ফলাফল", "val": "সর্বোচ্চ লাইন স্পিডেও API মেমোরিতে ০% বটলনেক"}
        ]
    },
    {
        "num": "08",
        "en_title": "PRODUCTION INTELLIGENCE & OVERHEAT SOLUTION",
        "bn_title": "লাইভ মনিটরিং ও দুর্ঘটনা রোধ",
        "pillar": "৪. AI অ্যানোমালি ও সেফটি",
        "objective": "প্রথমে আমরা কীভাবে প্রবলেমটা সলভ করি তা সহজ ধাপে দেখানো, আর তারপর ফ্যাক্টরিতে বাস্তবে কী ঘটেছিল তা খুব সহজ ও স্পষ্টভাবে বলা।",
        "speech": (
            "তিন নম্বর ফিচার হলো Production Intelligence — সহজ কথায়, প্রতিটি মেশিন লাইভ দেখে সমস্যা শুরুতেই থামিয়ে দেওয়া।\n\n"
            "▶ কীভাবে আমরা সমস্যার সমাধান করি:\n"
            "ধাপে ধাপে দেখুন আমরা ফ্লোরে মেশিনের সমস্যাগুলো কীভাবে সমাধান করি:\n"
            "প্রথমত, প্রতিটি মেশিনের সেন্সর প্রতি সেকেন্ডে MQTT-র মাধ্যমে লাইভ তাপমাত্রা ও গতির হিসাব আমাদের Digital Twin-এ পাঠায়।\n"
            "দ্বিতীয়ত, আমাদের ব্যাকএন্ড স্বয়ংক্রিয়ভাবে প্রতিটি সংখ্যা নিরাপদ সীমার সাথে মিলিয়ে দেখে।\n"
            "তৃতীয়ত, কোনো মেশিন অতিরিক্ত গরম হলে ড্যাশবোর্ড সাথে সাথে লাল হয়ে যায় এবং ৩ সেকেন্ডের মধ্যে শিফট সুপারভাইজারের কাছে SMS অ্যালার্ট পাঠায়।\n"
            "আর চতুর্থত, সুপারভাইজার চার্ট খুলে দেখেন ঠিক কখন তাপমাত্রা বাড়তে শুরু করেছিল এবং সাথে সাথে সেখানেই মেশিন ঠিক করে নেন।\n\n"
            "▶ বাস্তবে ফ্লোরে কী ঘটেছিল (Real Case):\n"
            "এবার বলি ক্লায়েন্টের ফ্লোরে বাস্তবে কী হয়েছিল:\n"
            "Stenter (স্টেন্টার) লাইন ০৩-এ কটন কাপড় চলছিল, যেখানে নিরাপদ তাপমাত্রার সীমা ছিল ১৮৫ ডিগ্রি সেলসিয়াস। হঠাৎ করে তাপমাত্রা বেড়ে ১৯২ ডিগ্রিতে উঠে যায়।\n"
            "আমাদের সিস্টেম আসার আগে, শত শত মিটার কাপড় পুড়ে বা হলুদ হয়ে যাওয়ার আগে কেউ বিষয়টা টের পেত না।\n\n"
            "▶ ফলাফল:\n"
            "কিন্তু এবার AutoTaskX ১৯২ ডিগ্রির সেই স্পাইকটি ধরে ফেলে এবং ৩ সেকেন্ডেরও কম সময়ে অ্যালার্ট পাঠিয়ে দেয়। সুপারভাইজার সাথে সাথে তাপমাত্রা কমিয়ে দেন, ফলে পুরো কাপড়ের ব্যাচটি কোনো অপচয় ছাড়াই বেঁচে যায়।"
        ),
        "tech_points": [
            {"label": "বাস্তব ঘটনা", "val": "Stenter চেম্বারের তাপমাত্রা ১৯২°C (সীমা ১৮৫°C)"},
            {"label": "AI ও Twin অ্যাকশন", "val": "তাৎক্ষণিক লাল ড্যাশবোর্ড অ্যালার্ট + ৩ সেকেন্ডে SMS"},
            {"label": "রুট ডায়াগনোসিস", "val": "হিস্ট্রি চার্টে তাপমাত্রা বাড়ার সঠিক সময় শনাক্ত"},
            {"label": "ব্যবসায়িক মূল্য", "val": "কাপড় পোড়া রোধ ও অনাকাঙ্ক্ষিত ডাউনটাইম হ্রাস"}
        ]
    },
    {
        "num": "09",
        "en_title": "TEXTILE OS & DIGITAL TWIN CORE",
        "bn_title": "ভিন্ন ভিন্ন মেশিনকে এক ডিজিটাল টুইনে আনা",
        "pillar": "২. Digital Twin কোর",
        "objective": "ফ্যাক্টরি ভিজিটে দেখা পুরোনো ও নতুন সব মেশিনকে কীভাবে একটি ইউনিফাইড Digital Twin-এ আনা হয়েছে তা সহজভাবে বলা।",
        "speech": (
            "এই স্লাইডটি আমাদের Digital Twin ইঞ্জিনের মূল কেন্দ্রবিন্দু দেখাচ্ছে — আমরা এর নাম দিয়েছি Textile OS।\n\n"
            "▶ ফ্যাক্টরি ভিজিটে যা দেখেছি:\n"
            "ক্লায়েন্টের ফ্যাক্টরি ভিজিট করার সময় আমরা সাথে সাথেই খেয়াল করি যে মেশিনগুলো একই ভাষায় কথা বলে না। তাদের কাছে আধুনিক জার্মান Stenter, ইতালিয়ান মেশিন, এমনকি ৩০ বছরের পুরোনো কন্ট্রোলারও ছিল। কেউ Modbus-এ কথা বলে, কেউ Siemens S7 ব্যবহার করে, আবার কেউ OPC-UA বা RS-485 ব্যবহার করে। তবুও ক্লায়েন্ট চেয়েছিলেন প্রতিটি মেশিন যেন একটি Digital Twin-এর ভেতরে আসে।\n\n"
            "▶ আমাদের সমাধান:\n"
            "তাই আমরা Textile OS-কে একটি স্মার্ট ট্রান্সলেটর লেয়ার হিসেবে তৈরি করি।\n"
            "আমাদের Edge Gateways প্রতিটি মেশিন থেকে তার নিজস্ব ভাষাতেই ডেটা পড়ে নেয় — যেমন তাপমাত্রা, আর্দ্রতা, স্টিম প্রেসার, গতি এবং বিদ্যুৎ খরচ।\n"
            "এজ লেভেল থেকেই আমরা ওই সব ভিন্ন ভিন্ন সিগন্যালকে একটি পরিষ্কার, স্ট্যান্ডার্ড JSON ফরম্যাটে রূপান্তর করি।\n"
            "সেই পরিষ্কার ডেটা স্ট্রিম আমাদের ব্যাকএন্ডে প্রতিটি মেশিনের একটি লাইভ ভার্চুয়াল টুইন আপডেট রাখে।\n\n"
            "▶ ফলাফল:\n"
            "মেশিন একদম নতুন হোক বা ৩০ বছরের পুরোনো, AutoTaskX-এর ভেতরে প্রতিটি মেশিন একটি পরিষ্কার Digital Twin নোড হিসেবে কাজ করে।"
        ),
        "tech_points": [
            {"label": "ভিজিট ফাইন্ডিং", "val": "মিশ্র ফ্লিট: আধুনিক ইউরোপীয় Stenter + ৩০ বছরের পুরোনো PLC"},
            {"label": "সাপোর্টেড প্রোটোকল", "val": "Modbus RTU/TCP, Siemens S7, OPC-UA, RS-485 Serial"},
            {"label": "Digital Twin লেয়ার", "val": "Textile OS এজে স্ট্যান্ডার্ড JSON স্কিমায় রূপান্তর"},
            {"label": "ভার্চুয়াল সিঙ্ক", "val": "প্রতিটি মেশিন একটি অভিন্ন Digital Twin নোড"}
        ]
    },
    {
        "num": "10",
        "en_title": "IOT DATA TRACE UNDER 25MS",
        "bn_title": "একটি সেন্সর রিডিংয়ের ২৫ মিলিসেকেন্ডের যাত্রা",
        "pillar": "২. ডেটা ট্রেস (<25ms)",
        "objective": "ইন্টারভিউয়ারকে স্লাইডের বাটনে ক্লিক করে <25ms লাইভ ডেটা ফ্লো দেখানো।",
        "speech": (
            "ক্লায়েন্ট সত্যিকারের রিয়েল-টাইম আপডেট চেয়েছিলেন, তাই ব্যাকএন্ডে বিলম্ব — অর্থাৎ latency (লেইটেন্সি) — একদম কম রাখা আমাদের জন্য খুব গুরুত্বপূর্ণ ছিল। চলুন Slide 10-এ একটি মাত্র তাপমাত্রার রিডিংয়ের যাত্রা অনুসরণ করি:\n\n"
            "প্রথমে Stenter মেশিনের ভেতরে একটি PT100 (পি-টি হান্ড্রেড) সেন্সর প্রতি ১০০ মিলিসেকেন্ডে ১৮৫.৫ ডিগ্রি রিডিং নেয়।\n"
            "এরপর IoT Gateway সেই সিগন্যালকে ছোট একটি MQTT প্যাকেটে রূপান্তর করে।\n"
            "প্যাকেটটি ফ্যাক্টরি নেটওয়ার্ক হয়ে আমাদের FastAPI ব্যাকএন্ডে পৌঁছায়।\n"
            "AutoTaskX নিরাপদ সীমা চেক করে, Digital Twin আপডেট করে, TimescaleDB-তে সেভ করে এবং লাইভ স্ক্রিনে পাঠিয়ে দেয়।\n\n"
            "আসুন স্লাইডের ওপর 'Animate Data Flow' বাটনে ক্লিক করে দেখি — আপনারা নিজের চোখেই দেখতে পাবেন ছয়টি ধাপই ২৫ মিলিসেকেন্ডের কম সময়ে শেষ হচ্ছে!"
        ),
        "tech_points": [
            {"label": "সেন্সর ট্রেস", "val": "PT100 RTD (185.5°C @ 100ms) -> Gateway -> MQTT -> UI"},
            {"label": "প্যাকেট ওভারহেড", "val": "অত্যন্ত হালকা ২-বাইট MQTT হেডার (QoS 1)"},
            {"label": "পাইপলাইন লেইটেন্সি", "val": "হার্ডওয়্যার থেকে লাইভ স্ক্রিনে <25ms এন্ড-টু-এন্ড"},
            {"label": "ইন্টারেক্টিভ ডেমো", "val": "Slide 10-এ 'Animate Data Flow' ক্লিক করে লাইভ দেখুন"}
        ]
    },
    {
        "num": "11",
        "en_title": "WHY MQTT? DATA TRANSPORT DECISION",
        "bn_title": "এম-কিউ-টি-টি কেন ব্যবহার করলাম?",
        "pillar": "৫. MQTT প্রোটোকল সিদ্ধান্ত",
        "objective": "কেন আমরা HTTP-র বদলে MQTT বেছে নিলাম এবং বড় ছবির জন্য কেন সরাসরি S3 ব্যবহার করলাম তা সহজভাবে বলা।",
        "speech": (
            "আপনাদের মনে প্রশ্ন আসতে পারে — সেন্সর ডেটার জন্য আমরা সাধারণ HTTP REST API-র বদলে কেন MQTT ব্যবহার করলাম?\n\n"
            "▶ সমস্যা:\n"
            "ভাবুন তো, ৫০টি মেশিন প্রতি সেকেন্ডে সাধারণ HTTP দিয়ে রিডিং পাঠাচ্ছে। HTTP-তে বড় হেডার থাকে এবং প্রতিবার নতুন কানেকশন খুলতে হয়। ফ্যাক্টরির দুর্বল Wi-Fi-তে এতে বিশাল বটলনেক তৈরি হয় এবং ডেটা ড্রপ করে।\n\n"
            "▶ আমাদের সমাধান:\n"
            "তাই আমরা সিস্টেমে দুটি সহজ নিয়ম সেট করি:\n"
            "নিয়ম এক: ছোট সেন্সর রিডিংগুলো যাবে আমাদের EMQX MQTT Broker-এর মাধ্যমে। তাপমাত্রা বা গতির ডেটা মাত্র কয়েক বাইটের হয়, আর MQTT Pub/Sub (পাব/সাব) চ্যানেলে খুব হালকা ২-বাইটের হেডার ব্যবহার করে — ফলে আমাদের Digital Twin একটি রিডিংও মিস করে না।\n"
            "নিয়ম দুই: ২০ মেগাবাইটের ভারী ছবি কখনোই MQTT-তে যাবে না। সেগুলো সরাসরি HTTPS দিয়ে AWS S3-তে যাবে, যাতে ব্রোকার একদম ফ্রি ও হালকা থাকে।\n\n"
            "▶ ফলাফল:\n"
            "পুরো ফ্যাক্টরি ফ্লোর জুড়ে আমরা দ্রুত ও নির্ভরযোগ্য কমিউনিকেশন পাই।"
        ),
        "tech_points": [
            {"label": "প্রোটোকল বিভাজন", "val": "ছোট সেন্সর ডেটায় MQTT বনাম ছবির জন্য HTTPS S3"},
            {"label": "কেন EMQX MQTT", "val": "সবসময় খোলা কানেকশন, কম ব্যান্ডউইথ ও জিরো-ড্রপ QoS"},
            {"label": "কেন ডিরেক্ট S3", "val": "২০MB ভিশন ফাইল MQTT ব্রোকারের মেমোরির বাইরে রাখে"},
            {"label": "Digital Twin ফিড", "val": "হাই-ফ্রিকোয়েন্সি Pub/Sub স্ট্রিমে টুইন লাইভ আপডেট"}
        ]
    },
    {
        "num": "12",
        "en_title": "STORAGE ARCHITECTURE",
        "bn_title": "তিনটি বিশেষায়িত ডেটাবেজ কেন?",
        "pillar": "৫. পলিগ্লট ডেটা স্টোরেজ",
        "objective": "৩টি আলাদা ডেটাবেজ কেন ব্যবহার করা হয়েছে তা খুব সহজ যুক্তিতে বোঝানো।",
        "speech": (
            "একজন Data Engineer হিসেবে সব ধরনের ডেটা একটিমাত্র ডেটাবেজে রাখলে সিস্টেম দ্রুত স্লো হয়ে যায়। তাই আমরা প্রতিটি কাজের ধরন অনুযায়ী তিনটি আলাদা স্টোরেজ বেছে নিয়েছি:\n\n"
            "প্রথমত, ব্যবসার রেকর্ডের জন্য PostgreSQL — যেমন বায়ার অর্ডার, ইউজার অ্যাকাউন্ট, মেশিন প্রোফাইল এবং ডাই রেসিপি, যেখানে ডেটার নির্ভুলতা সবচেয়ে জরুরি।\n\n"
            "দ্বিতীয়ত, সময়ভিত্তিক সেন্সর ডেটার জন্য TimescaleDB। যেহেতু আমরা লাখ লাখ সেন্সর রো সেভ করি, সাধারণ টেবিল সময়ের সাথে সাথে খুব ধীর হয়ে যায়। TimescaleDB চলে PostgreSQL-এর ভেতরেই — এটি Hypertables (হাইপার-টেবলস) ব্যবহার করে নিজে থেকেই সময় অনুযায়ী ডেটা ভাগ করে এবং স্টোরেজ স্পেস ৯৫ শতাংশ পর্যন্ত কমিয়ে দেয়!\n\n"
            "আর তৃতীয়ত, ভারী ফাইলের জন্য AWS S3 — যেমন কাপড় স্ক্যানের ছবি ও PDF রিপোর্ট।\n\n"
            "ফলে কোনো ম্যানেজার যখন ব্যাচের হিস্ট্রি চেক করেন, তিনটি স্টোরেজই পাশাপাশি দারুণ দ্রুতগতিতে কাজ করে।"
        ),
        "tech_points": [
            {"label": "স্টোরেজ কৌশল", "val": "কাজের ধরন অনুযায়ী তিনটি বিশেষায়িত ডেটাবেজ"},
            {"label": "PostgreSQL", "val": "অর্ডার, ইউজার, ডাই রেসিপি ও ব্যাচের ACID রেকর্ড"},
            {"label": "TimescaleDB", "val": "Hypertables অটো-চাংকিং ও ৯৫% স্টোরেজ কম্প্রেশন"},
            {"label": "AWS S3", "val": "২০MB TIFF কাপড় স্ক্যান ও জেনারেটেড PDF রিপোর্ট"}
        ]
    },
    {
        "num": "13",
        "en_title": "REAL-TIME DELIVERY PIPELINE",
        "bn_title": "লাইভ আপডেট বনাম হিস্টোরিক্যাল রিপোর্ট",
        "pillar": "২. রিয়েল-টাইম ডেটা সার্ভিং",
        "objective": "অপারেটরের লাইভ স্ক্রিন আর ডিরেক্টরের হিস্টোরিক্যাল রিপোর্ট আলাদা চ্যানেলে রাখার কারণ সহজভাবে বলা।",
        "speech": (
            "ডেটা সেভ করা কাজের অর্ধেক — বিভিন্ন মানুষের কাছে তা পরিষ্কারভাবে পৌঁছে দেওয়াটাও ঠিক ততটাই গুরুত্বপূর্ণ।\n\n"
            "▶ সমস্যা:\n"
            "ফ্লোরের কর্মীদের পেজ রিফ্রেশ না করেই তাৎক্ষণিক লাইভ আপডেট দরকার। অন্যদিকে, ক্লায়েন্টের ডিরেক্টররা কয়েক সপ্তাহের শিফট ডেটা নিয়ে ভারী চার্ট লোড করেন। দুটোই একই চ্যানেলে চললে বড় একটি রিপোর্ট লাইভ স্ক্রিনকে ফ্রিজ করে দিতে পারত।\n\n"
            "▶ আমাদের সমাধান:\n"
            "তাই আমরা ডেলিভারি রাস্তাটিকে দুটি আলাদা লেনে ভাগ করে দিই:\n"
            "ফ্লোরের লাইভ স্ক্রিনের জন্য FastAPI WebSockets কোনো অপেক্ষা ছাড়াই Digital Twin-এর পরিবর্তন সরাসরি Next.js ড্যাশবোর্ডে পুশ করে।\n"
            "আর অতীতের ট্রেন্ড ও শিফট রিপোর্টের জন্য আমরা TimescaleDB-র সামারি থেকে ক্যাশ করা REST API ব্যবহার করি।\n\n"
            "▶ ফলাফল:\n"
            "কোনো ডিরেক্টর যখন ৩০ দিনের এনার্জি রিপোর্ট লোড করেন, তখনও ফ্লোরের লাইভ মেশিন স্ক্রিন একদম সুপার ফাস্ট থাকে।"
        ),
        "tech_points": [
            {"label": "ডুয়াল চ্যানেল", "val": "WebSockets (লাইভ ফ্লোর) + Cached REST API (রিপোর্ট)"},
            {"label": "ফ্লোর অপারেটর", "val": "জিরো-পোলিং লাইভ Digital Twin স্ক্রিন (<25ms)"},
            {"label": "ম্যানেজমেন্ট", "val": "৩০ দিনের ভারী ট্রেন্ড ও শিফট এনার্জি অ্যানালিটিক্স"},
            {"label": "পারফরম্যান্স", "val": "ভারী রিপোর্ট কখনো রিয়েল-টাইম মনিটরিং আটকায় না"}
        ]
    },
    {
        "num": "14",
        "en_title": "FEATURE 05 — ERP INTEGRATION",
        "bn_title": "ফ্যাক্টরি থেকে অফিসের ই-আর-পি অটোমেশন",
        "pillar": "৩. এন্টারপ্রাইজ ERP ব্রিজ",
        "objective": "ক্লায়েন্টের অফিসের ERP সফটওয়্যারের সাথে ফ্যাক্টরি ফ্লোর কীভাবে অটোমেটিক যুক্ত হলো তা বলা।",
        "speech": (
            "পাঁচ নম্বর ফিচারটি এমন একটি গ্যাপ পূরণ করে যা ক্লায়েন্ট আমাদের প্রথম অফিস মিটিংয়েই সরাসরি চেয়েছিলেন — ফ্যাক্টরি ফ্লোরকে তাদের হেড-অফিসের ERP সফটওয়্যারের সাথে যুক্ত করা।\n\n"
            "▶ সমস্যা:\n"
            "অধিকাংশ বড় টেক্সটাইল গ্রুপের মতোই ক্লায়েন্ট আগে থেকেই SAP, Datatex NOW, বা Infor M3-এর মতো ERP ব্যবহার করতেন। AutoTaskX-এর আগে স্টাফরা কাগজে উৎপাদনের হিসাব লিখতেন, আর কেউ এক-দুই দিন পর সেটা ERP-তে টাইপ করতেন — যেখানে প্রায়ই ভুল হতো।\n\n"
            "▶ আমাদের সমাধান:\n"
            "তাই আমরা একটি টু-ওয়ে ERP ব্রিজ তৈরি করি:\n"
            "ওয়ার্ক অর্ডারগুলো ERP থেকে সরাসরি ডিজিটাল জব হিসেবে AutoTaskX-এ চলে আসে।\n"
            "আর ডাইং বা ইন্সপেকশন ব্যাচ শেষ হওয়ার সাথে সাথে প্রকৃত কত মিটার কাপড় তৈরি হলো এবং ঠিক কতটুকু কেমিক্যাল খরচ হলো তা অটোমেটিক ERP-র স্টক রেকর্ডে সিঙ্ক হয়ে যায়।\n\n"
            "▶ ফলাফল:\n"
            "দুই দিনের কোনো দেরি নেই, ম্যানুয়াল টাইপিংয়ের ভুল নেই, এবং ক্লায়েন্টের জন্য ১০০ শতাংশ স্বচ্ছ স্টক ট্র্যাকিং নিশ্চিত হয়েছে।"
        ),
        "tech_points": [
            {"label": "ERP চাহিদা", "val": "SAP / Datatex-এ ২৪–৪৮ ঘণ্টার ম্যানুয়াল দেরি দূর করা"},
            {"label": "ওয়ার্ক অর্ডার ডাউন", "val": "ERP অর্ডার স্বয়ংক্রিয়ভাবে ডিজিটাল শপফ্লোর জব হয়"},
            {"label": "আউটপুট সিঙ্ক আপ", "val": "আসল মিটার ও কেমিক্যাল খরচ ERP স্টকে অটো-আপডেট"},
            {"label": "অডিট ইমপ্যাক্ট", "val": "১০০% পেপারলেস ও নির্ভুল স্টক ট্র্যাকিং"}
        ]
    },
    {
        "num": "15",
        "en_title": "COMPLETE 4-ZONE ARCHITECTURE",
        "bn_title": "পুরো সিস্টেমের ৪-জোন ব্লুপ্রিন্ট",
        "pillar": "২. ৪-জোন স্কেলেবল ব্লুপ্রিন্ট",
        "objective": "৪টি জোনে পুরো আর্কিটেকচার ব্লুপ্রিন্ট এক নজরে দেখানো এবং এটি কত সহজে স্কেল করা যায় তা বলা।",
        "speech": (
            "এই স্লাইডে তাকালে দেখবেন, চারটি স্পষ্ট জোনে আমাদের পুরো আর্কিটেকচার ব্লুপ্রিন্ট সাজানো আছে:\n\n"
            "জোন এক হলো Physical Factory — স্টেন্টার, ডাইং মেশিন, লুম, ক্যামেরা এবং ১০০টিরও বেশি সেন্সর।\n"
            "জোন দুই হলো Connection Layer — Edge Gateways যা Modbus বা OPC-UA পড়ে আমাদের EMQX MQTT Broker-এ পাঠায়।\n"
            "জোন তিন হলো Core & Storage Layer — আমাদের FastAPI ব্যাকএন্ড, AI ভিশন মডেল, Digital Twin স্টেট এবং তিনটি ডেটাবেজ: PostgreSQL, TimescaleDB ও AWS S3।\n"
            "জোন চার হলো Delivery & Business Apps — Next.js ড্যাশবোর্ড, মোবাইল অ্যাপ, SMS অ্যালার্ট এবং ERP ব্রিজ।\n\n"
            "আর ক্লায়েন্ট চেয়েছিলেন যেন ভবিষ্যতে তারা সহজে ফ্যাক্টরি বড় করতে পারেন। যেহেতু প্রতিটি লেয়ার পরিষ্কারভাবে আলাদা করা, কালকে যদি তারা আরেকটি বিল্ডিংয়ে ৫০টি নতুন মেশিন যোগ করেন, আমাদের শুধু জোন এক ও দুই-এ গেটওয়ে যোগ করতে হবে — মূল কোডে কোনো পরিবর্তনেরই প্রয়োজন হবে না।"
        ),
        "tech_points": [
            {"label": "জোন ১ ও জোন ২", "val": "১০০+ ফ্লোর সেন্সর -> Edge Gateways -> EMQX MQTT"},
            {"label": "জোন ৩ (কোর)", "val": "FastAPI, AI মডেল, Digital Twin ও ৩টি ডেটাবেজ"},
            {"label": "জোন ৪ (অ্যাপস)", "val": "Next.js ড্যাশবোর্ড, মোবাইল QA, SMS ও ERP কানেক্টর"},
            {"label": "ক্লায়েন্ট সম্প্রসারণ", "val": "মূল কোড না বদলেই ৫০+ নতুন মেশিন যোগ করার সুবিধা"}
        ]
    },
    {
        "num": "16",
        "en_title": "MEASURABLE BUSINESS OUTCOMES",
        "bn_title": "গাজীপুর মিলে বাস্তব ফলাফল ও আরওআই",
        "pillar": "৬. ক্লায়েন্ট ROI ও ইমপ্যাক্ট",
        "objective": "গাজীপুর টেক্সটাইল মিলে পাওয়া বাস্তব ও সন্তোষজনক ফলাফলগুলো তুলে ধরা।",
        "speech": (
            "দিনের শেষে ভালো ইঞ্জিনিয়ারিংয়ের সার্থকতা হলো বাস্তব ব্যবসায়িক সাফল্য এনে দেওয়া। এই স্লাইডে আপনারা ক্লায়েন্টের গাজীপুর টেক্সটাইল মিল নম্বর ৪-এর লাইভ সংখ্যাগুলো দেখতে পাচ্ছেন:\n\n"
            "সংযুক্ত ২৬টি মেশিনের মধ্যে ২৪টি এখন বিরামহীনভাবে চলছে, আর ২টি পূর্ব-পরিকল্পিত মেইনটেন্যান্সের জন্য অফলাইনে আছে — অর্থাৎ এখন আর কিছুই আড়ালে থাকে না।\n"
            "স্টেন্টারের তাপমাত্রা ১৮৫.৫ ডিগ্রিতে স্থির আছে এবং কোনো ক্রিটিক্যাল অ্যালার্ট নেই।\n"
            "এক দিনে আমরা রিয়েল-টাইমে ৪২,৫০০ মিটার কাপড় ট্র্যাক করেছি।\n"
            "AI ভিশন ইন্সপেকশনের মাধ্যমে Right-First-Time (রাইট-ফার্স্ট-টাইম) কোয়ালিটি পাস রেট ৯৯.২ শতাংশে পৌঁছেছে।\n"
            "আর সামগ্রিক মেশিন দক্ষতা — যাকে OEE (ও-ই-ই) বলা হয় — মাত্র চার মাসেই ১৪ শতাংশ বেড়েছে।\n\n"
            "এখন ক্লায়েন্ট বিশ্বের যেকোনো প্রান্ত থেকে শুধু একটি ট্যাবলেট খুলেই দেখতে পারেন তাদের পুরো ফ্যাক্টরি কেমন চলছে।"
        ),
        "tech_points": [
            {"label": "ক্লায়েন্ট ডিপ্লয়মেন্ট", "val": "গাজীপুর টেক্সটাইল মিল #০৪ — ২৬টি সংযুক্ত মেশিন"},
            {"label": "ফ্লিট স্ট্যাটাস", "val": "২৪টি লাইভ চালু · ২টি পরিকল্পিত মেইনটেন্যান্স · ০ অ্যালার্ট"},
            {"label": "দৈনিক থ্রুপুট", "val": "৪২,৫০০মি. লাইভ ট্র্যাকড · ৯৯.২% ভিশন পাস রেট (RFT)"},
            {"label": "ক্লায়েন্ট ROI", "val": "মাত্র ৪ মাসে +১৪% OEE দক্ষতা বৃদ্ধি"}
        ]
    },
    {
        "num": "17",
        "en_title": "AI AUTOMATION & FUTURE ROADMAP",
        "bn_title": "এ-আই অটোমেশন ও ভবিষ্যৎ পরিকল্পনা",
        "pillar": "২. AI ও অটোনোমাস রোডম্যাপ",
        "objective": "ভবিষ্যতের AI Automation ও Predictive Maintenance পরিকল্পনা সহজ ও স্মার্টভাবে তুলে ধরা।",
        "speech": (
            "প্রথম চার মাসের ফলাফল এত ভালো হওয়ায় আমরা ক্লায়েন্টের সাথে আরও স্মার্ট AI Automation যুক্ত করার জন্য পাঁচ ধাপের একটি ভবিষ্যৎ রোডম্যাপ তৈরি করেছি:\n\n"
            "ধাপ এক হলো Connect More — ফ্যাক্টরির বাকি মেশিনগুলোকেও একই Digital Twin-এ যুক্ত করা, যাতে ক্লায়েন্ট ১০০ শতাংশ লাইভ কভারেজ পান।\n"
            "ধাপ দুই হলো Full Auto Inspection — যেখানে ক্যামেরা নিজে থেকেই প্রতিটি মিটার কাপড় চেক করবে, কর্মীদের আর ম্যানুয়ালি ছবি তুলতে হবে না।\n"
            "ধাপ তিন হলো Smart Past Data — কয়েক মাসের TimescaleDB ডেটা ব্যবহার করে শীত ও গ্রীষ্মকালে রঙ কীভাবে আচরণ করে তা আগে থেকেই অনুমান করা।\n"
            "ধাপ চার হলো Predictive Maintenance (প্রিডিক্টিভ মেইনটেন্যান্স) — মোটরের কম্পন ও বাড়তি তাপমাত্রা পর্যবেক্ষণ করে কোনো মেশিন নষ্ট হওয়ার আগেই AI টিমকে সতর্ক করবে।\n"
            "এবং ধাপ পাঁচ হলো Closed-Loop Control (ক্লোজড-লুপ কন্ট্রোল) — যেখানে Digital Twin নিজেই নিরাপদে সরাসরি মেশিনের PLC-তে ছোটখাটো গতি বা তাপমাত্রার অ্যাডজাস্টমেন্ট পাঠিয়ে দেবে।"
        ),
        "tech_points": [
            {"label": "ধাপ ১ ও ২", "val": "১০০% মিল কভারেজ + অটোমেটেড ইনলাইন ট্রিগার"},
            {"label": "ধাপ ৩ (অ্যানালিটিক্স)", "val": "মৌসুমী রঙের আচরণে TimescaleDB হিস্টোরিক্যাল AI"},
            {"label": "ধাপ ৪ (AI PdM)", "val": "ভাইব্রেশন ও বিয়ারিং তাপে Predictive Maintenance"},
            {"label": "ধাপ ৫ (স্বয়ংক্রিয়)", "val": "PLC গতি ও তাপ নিয়ন্ত্রণে Closed-Loop Digital Twin"}
        ]
    },
    {
        "num": "18",
        "en_title": "CONCLUSION & Q&A",
        "bn_title": "সমাপ্তি ও প্রশ্নোত্তর পর্ব",
        "pillar": "৬. সমাপ্তি ও প্রশ্নোত্তর",
        "objective": "আত্মবিশ্বাসের সাথে প্রজেক্টের মূল কথা শেষ করে ইন্টারভিউয়ারকে প্রশ্নের জন্য আমন্ত্রণ জানানো।",
        "speech": (
            "সবশেষে এটাই বলব, AutoTaskX কেবল কোনো ডেমো বা থিওরি নয়। এর শুরু হয়েছিল যখন বাংলাদেশের একটি শীর্ষস্থানীয় টেক্সটাইল ক্লায়েন্ট পূর্ণ অটোমেশন ও লাইভ Digital Twin চেয়ে আমাদের অফিসে আসেন। ফ্যাক্টরি ভিজিট করে রিকোয়ারমেন্টস সংগ্রহ এবং সফটওয়্যার ব্লুপ্রিন্ট তৈরির পর আমাদের তিনজন ডেভেলপারের কোর টিম মাত্র চার মাসে এর ব্যাকএন্ড ও ফ্রন্টএন্ড দাঁড় করায় — আর মূল ব্যাকএন্ড ইঞ্জিনিয়ারদের একজন হিসেবে প্রায় ৪০ থেকে ৫০ শতাংশ কাজ করার পর সিস্টেমটিকে বাস্তব ফ্যাক্টরিতে ২৪/৭ চলতে দেখা সত্যিই দারুণ অনুভূতি।\n\n"
            "পরিষ্কার Data Engineering, দ্রুতগতির MQTT স্ট্রিমিং, লাইভ Digital Twin আপডেট এবং বাস্তবসম্মত AI Automation-এর সমন্বয়ে আমরা বিচ্ছিন্ন মেশিনগুলোকে একটি সংযুক্ত স্মার্ট মিলে পরিণত করেছি।\n\n"
            "মনোযোগ দিয়ে শোনার জন্য আপনাদের অসংখ্য ধন্যবাদ! আমাদের ব্যাকএন্ড আর্কিটেকচার, Digital Twin সেটআপ, MQTT ফ্লো বা AI পাইপলাইন নিয়ে আপনাদের যেকোনো প্রশ্নের উত্তর দিতে পারলে আমি খুব খুশি হবো — দয়া করে যেকোনো প্রশ্ন করতে পারেন।"
        ),
        "tech_points": [
            {"label": "প্রজেক্টের যাত্রা", "val": "অফিস মিটিং → ফ্যাক্টরি ভিজিট → ব্লুপ্রিন্ট → ২৪/৭ লাইভ"},
            {"label": "টিম অবদান", "val": "৩-জনের কোর টিম · মূল ব্যাকএন্ড (~৪০–৫০%)"},
            {"label": "মূল ভিত্তি", "val": "Digital Twin · EMQX MQTT · Data Pipeline · AI Vision"},
            {"label": "প্রশ্নোত্তর প্রস্তুতি", "val": "আর্কিটেকচার, পাইপলাইন ও ডেটা ডিপ ডাইভের জন্য প্রস্তুত"}
        ]
    }
]

bangla_cheat_questions = [
    {
        "num": "১",
        "title": "ফিজিক্যাল মেশিনের সাথে Digital Twin-কে সবসময় কীভাবে সিঙ্ক রাখেন?",
        "answer": (
            "প্রতিটি মেশিনে একটি Edge Gateway থাকে যা প্রতি ১০০ মিলিসেকেন্ডে সেন্সর রিডিং পড়ে। এটি রিডিংগুলোকে পরিষ্কার JSON ফরম্যাটে রূপান্তর করে MQTT-র মাধ্যমে আমাদের EMQX Broker-এ পাঠায়। আমাদের FastAPI ব্যাকএন্ড সাথে সাথে সেটি রিসিভ করে, মেমোরিতে থাকা Digital Twin আপডেট করে, ইতিহাস হিসেবে TimescaleDB-তে সেভ করে এবং WebSockets-এর মাধ্যমে ড্যাশবোর্ডে লাইভ আপডেট পুশ করে — পুরো কাজটাই ২৫ মিলিসেকেন্ডের কম সময়ে সম্পন্ন হয়।"
        )
    },
    {
        "num": "২",
        "title": "সেন্সর ডেটার জন্য সাধারণ HTTP API-র বদলে MQTT কেন বেছে নিলেন?",
        "answer": (
            "সাধারণ ওয়েব পেজের জন্য HTTP ভালো, কিন্তু যখন সেন্সর প্রতি সেকেন্ডে ডেটা পাঠায়, তখন HTTP-র বড় হেডার সিস্টেমকে ভারী ও ধীর করে দেয় — বিশেষ করে ফ্যাক্টরির Wi-Fi-তে এটি বড় বটলনেক তৈরি করে। অন্যদিকে, MQTT একটি সার্বক্ষণিক খোলা কানেকশনের ওপর মাত্র ২-বাইটের ছোট হেডার ব্যবহার করে। তাছাড়া QoS Level 1 থাকায় ফ্যাক্টরির Wi-Fi এক মুহূর্তের জন্য দুর্বল হলেও মেশিনের গুরুত্বপূর্ণ রিডিং হারিয়ে যায় না।"
        )
    },
    {
        "num": "৩",
        "title": "TimescaleDB কেন ব্যবহার করলেন? শুধু PostgreSQL বা MongoDB নয় কেন?",
        "answer": (
            "আসলে ক্লায়েন্টের জন্য আমাদের দুই ধরনের সুবিধাই দরকার ছিল। অর্ডার আর ডাই রেসিপির জন্য পরিষ্কার রিলেশনাল টেবিল লাগে, যেখানে PostgreSQL আমাদের নিখুঁত ACID নিশ্চয়তা দেয়। কিন্তু সাধারণ টেবিলে লাখ লাখ সেন্সর রো জমলে সময়ের সাথে সার্চ খুব স্লো হয়ে যায়। যেহেতু TimescaleDB চলে PostgreSQL-এর ভেতরেই এবং সময়ভিত্তিক Hypertables (হাইপার-টেবলস) ব্যবহার করে, এটি নিজে থেকেই সময় অনুযায়ী ডেটা ভাগ করে এবং ৯৫ শতাংশ পর্যন্ত ডিস্ক স্পেস বাঁচায় — সবই একই ডেটাবেজ সিস্টেমের ভেতর।"
        )
    },
    {
        "num": "৪",
        "title": "২০ মেগাবাইটের ইন্সপেকশন ছবি আপলোডের সময় ফ্যাক্টরির ইন্টারনেট চলে গেলে কী হয়?",
        "answer": (
            "ফ্যাক্টরি ভিজিটের সময়ই আমরা এই বাস্তব সমস্যার কথা দেখেছিলাম, তাই এজ লেভেলেই এর সমাধান রেখেছি। Edge PC-তে আমরা একটি লোকাল FIFO disk queue (ফিফো ডিস্ক কিউ) তৈরি করেছি। প্রতিটি ছবি প্রথমে লোকাল ডিস্কে সেভ হয়, এবং AWS S3 সফল আপলোডের কনফার্মেশন না দেওয়া পর্যন্ত আমরা সেটি ডিলিট করি না। ইন্টারনেট ফিরে এলেই অপেক্ষায় থাকা ছবিগুলো ঠিক ক্রম অনুযায়ী আপলোড হয়ে যায় — একটি ফ্রেমও হারায় না।"
        )
    },
    {
        "num": "৫",
        "title": "ব্যাকএন্ডের জন্য Django-র বদলে FastAPI কেন বেছে নিলেন?",
        "answer": (
            "আমাদের একসাথে শত শত লাইভ IoT স্ট্রিম এবং WebSocket ড্যাশবোর্ড চালাতে হচ্ছিল। Django মূলত সাধারণ একের পর এক ওয়েব রিকোয়েস্টের জন্য তৈরি, তাই বিরামহীন স্ট্রিমিংয়ের ক্ষেত্রে কিছুটা ভারী হয়ে যায়। অন্যদিকে, FastAPI-তে বিল্ট-ইন AsyncIO সাপোর্ট থাকায় এটি অনেক কম CPU ও মেমোরি খরচ করে একসাথে অসংখ্য লাইভ MQTT ও WebSocket কানেকশন সহজেই সামলাতে পারে।"
        )
    },
    {
        "num": "৬",
        "title": "এখানে AI Automation শুধু নামমাত্র না হয়ে বাস্তবে কীভাবে সাহায্য করছে?",
        "answer": (
            "সত্যি বলতে, ক্লায়েন্ট শুধু দেখানোর জন্য AI চাননি — তারা বাস্তব ব্যবসায়িক ফলাফল চেয়েছিলেন। তাই আমরা তিনটি বাস্তবসম্মত জায়গায় AI ব্যবহার করেছি: প্রথমত, OpenCV ও YOLO দিয়ে মিনিটে ১২০ মিটার গতিতে ০.৫ মিলিমিটারের চেয়ে ছোট কাপড়ের ত্রুটি ধরা; দ্বিতীয়ত, স্মার্ট হিট অ্যালার্ট যা ১৯২ ডিগ্রিতে কাপড় পুড়ে যাওয়া আটকে দিয়েছে; এবং তৃতীয়ত, TimescaleDB-তে পরিষ্কার হিস্টোরিক্যাল ডেটা জমিয়ে রাখা যাতে Predictive Maintenance-এর মাধ্যমে মোটরের ভাইব্রেশন সমস্যা আগেই ধরা যায়।"
        )
    }
]

with open('guide_data_bd.json', 'w', encoding='utf-8') as out_f_bd:
    json.dump({'slides': bangla_slides, 'cheat_questions': bangla_cheat_questions}, out_f_bd, ensure_ascii=False, indent=2)

print(f"Generated {len(bangla_slides)} slides and {len(bangla_cheat_questions)} questions into guide_data_bd.json.")
