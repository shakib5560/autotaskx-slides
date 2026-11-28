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
