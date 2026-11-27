import json
import html
import re

with open('guide_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slides = data['slides']
cheat_questions = data['cheat_questions']

# Format speech text: convert line breaks and format technical terms for easy reading
def format_speech(text):
    text = html.escape(text)
    tech_keywords = [
        'FastAPI', 'MQTT', 'TimescaleDB', 'PostgreSQL', 'Postgres', 'AWS S3', 'S3',
        'CoaXPress', 'Basler', 'Kubelka-Munk', 'Digital Twin', 'EMQX', 'WebSocket',
        'WebSockets', 'Next.js', 'OpenCV', 'YOLO', 'Modbus', 'Modbus RTU/TCP', 'OPC-UA',
        'RS-485', 'PT100', 'Pre-signed S3 URL', 'Pre-signed URL', 'Pre-signed',
        'Right-First-Time', 'RFT', 'OEE', 'ΔE', 'Delta-E', 'FIFO', 'AsyncIO', 'ASGI', 'WSGI',
        'SAP', 'ERP', 'AI Automation', 'Data Pipeline', 'Data Engineering', 'Edge Gateway',
        'Hypertable', 'Predictive Maintenance', 'Textile OS'
    ]
    ordered_kws = sorted(set(tech_keywords), key=len, reverse=True)
    combined = re.compile(r'(?<![\w\-])(' + '|'.join(re.escape(k) for k in ordered_kws) + r')(?![\w\-])')
    text = combined.sub(r'<span class="tech-inline">\1</span>', text)

    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    out = ""
    for p in paragraphs:
        out += f"<p>{p.replace(chr(10), '<br>')}</p>"
    return out

html_content = f"""<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AutoTaskX — Digital Twin &amp; Data Engineer English Presentation Guide</title>
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230B132B'/%3E%3Ctext x='50%25' y='54%25' dominant-baseline='middle' text-anchor='middle' font-family='Inter,Arial,sans-serif' font-weight='800' font-size='26' fill='%2338BDF8'%3EAX%3C/text%3E%3C/svg%3E">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #F6F7F5;
            --bg-card: #FFFFFF;
            --bg-sidebar: #FFFFFF;
            --bg-header: rgba(255, 255, 255, 0.94);
            --border: #E2E5DF;
            --border-light: #EDF0EB;
            --text-main: #141816;
            --text-secondary: #4A524D;
            --text-muted: #737D77;
            --navy-primary: #0B132B;
            --navy-surface: #1C2541;
            --accent-blue: #2563EB;
            --accent-blue-bg: #EFF6FF;
            --accent-green: #059669;
            --accent-green-bg: #ECFDF5;
            --accent-amber: #D97706;
            --accent-amber-bg: #FFFBEB;
            --accent-purple: #7C3AED;
            --accent-purple-bg: #F5F3FF;
            --card-shadow: 0 2px 8px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02);
            --card-hover: 0 8px 24px rgba(0, 0, 0, 0.06);
            --font-ui: 'Inter', 'Hind Siliguri', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-bn: 'Inter', 'Hind Siliguri', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            --base-font-size: 16px;
        }}

        [data-theme="dark"] {{
            --bg-body: #080C14;
            --bg-card: #0F1626;
            --bg-sidebar: #0B1220;
            --bg-header: rgba(11, 18, 32, 0.94);
            --border: #1F2A3F;
            --border-light: #162032;
            --text-main: #F1F5F9;
            --text-secondary: #CBD5E1;
            --text-muted: #8896AB;
            --navy-primary: #38BDF8;
            --navy-surface: #1E293B;
            --accent-blue: #60A5FA;
            --accent-blue-bg: #172554;
            --accent-green: #34D399;
            --accent-green-bg: #064E3B;
            --accent-amber: #FBBF24;
            --accent-amber-bg: #451A03;
            --accent-purple: #A78BFA;
            --accent-purple-bg: #2E1065;
            --card-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            --card-hover: 0 8px 28px rgba(0, 0, 0, 0.45);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        html {{
            font-size: var(--base-font-size);
            scroll-behavior: smooth;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: var(--font-bn);
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
            transition: background-color 0.25s ease, color 0.25s ease;
        }}

        /* Header Bar */
        .site-header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-header);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
            padding: 0.75rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }}

        .brand-area {{
            display: flex;
            align-items: center;
            gap: 0.85rem;
        }}

        .brand-logo {{
            width: 32px;
            height: 32px;
            background: #0B132B;
            color: #FFFFFF;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-ui);
            font-weight: 800;
            font-size: 0.95rem;
            letter-spacing: -0.5px;
            box-shadow: 0 2px 6px rgba(11, 19, 43, 0.3);
        }}

        .brand-text h1 {{
            font-family: var(--font-ui);
            font-size: 1.02rem;
            font-weight: 700;
            letter-spacing: -0.3px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .badge-role {{
            background: var(--accent-purple-bg);
            color: var(--accent-purple);
            font-size: 0.72rem;
            font-family: var(--font-ui);
            font-weight: 700;
            padding: 0.2rem 0.55rem;
            border-radius: 6px;
            border: 1px solid rgba(124, 58, 237, 0.25);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .badge-live {{
            background: var(--accent-green-bg);
            color: var(--accent-green);
            font-size: 0.7rem;
            font-family: var(--font-ui);
            font-weight: 700;
            padding: 0.2rem 0.5rem;
            border-radius: 9999px;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            border: 1px solid rgba(5, 150, 105, 0.25);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .badge-live::before {{
            content: "";
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent-green);
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.4; transform: scale(0.85); }}
        }}

        .header-controls {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }}

        .search-box {{
            position: relative;
            display: flex;
            align-items: center;
        }}

        .search-box input {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-main);
            font-family: var(--font-ui);
            font-size: 0.85rem;
            padding: 0.45rem 0.85rem 0.45rem 2rem;
            border-radius: 8px;
            width: 220px;
            transition: all 0.2s ease;
        }}

        .search-box input:focus {{
            outline: none;
            border-color: var(--accent-blue);
            width: 280px;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
        }}

        .search-icon {{
            position: absolute;
            left: 0.7rem;
            width: 14px;
            height: 14px;
            fill: none;
            stroke: var(--text-muted);
            stroke-width: 2;
        }}

        .btn-ctrl {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-secondary);
            font-family: var(--font-ui);
            font-size: 0.82rem;
            font-weight: 600;
            padding: 0.45rem 0.75rem;
            border-radius: 8px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.15s ease;
            text-decoration: none;
        }}

        .btn-ctrl:hover {{
            background: var(--border-light);
            color: var(--text-main);
            border-color: var(--text-muted);
        }}

        .btn-deck {{
            background: #0B132B;
            color: #FFFFFF;
            border-color: #0B132B;
        }}

        .btn-deck:hover {{
            background: #1C2541;
            color: #FFFFFF;
        }}

        /* App Layout */
        .app-container {{
            display: flex;
            max-width: 1540px;
            margin: 0 auto;
            position: relative;
        }}

        /* Sidebar */
        .sidebar {{
            width: 320px;
            flex-shrink: 0;
            position: sticky;
            top: 56px;
            height: calc(100vh - 56px);
            overflow-y: auto;
            padding: 1.25rem 1rem 3rem 1.5rem;
            border-right: 1px solid var(--border);
            background: var(--bg-sidebar);
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }}

        .sidebar-heading {{
            font-family: var(--font-ui);
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--text-muted);
            margin: 0.85rem 0.5rem 0.4rem 0.5rem;
        }}

        .nav-item {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            padding: 0.55rem 0.75rem;
            border-radius: 8px;
            color: var(--text-secondary);
            text-decoration: none;
            font-family: var(--font-ui);
            font-size: 0.82rem;
            font-weight: 500;
            transition: all 0.15s ease;
            line-height: 1.35;
            border-left: 3px solid transparent;
        }}

        .nav-item:hover {{
            background: var(--border-light);
            color: var(--text-main);
        }}

        .nav-item.active {{
            background: var(--accent-blue-bg);
            color: var(--accent-blue);
            font-weight: 600;
            border-left-color: var(--accent-blue);
        }}

        .nav-num {{
            font-family: var(--font-mono);
            font-size: 0.72rem;
            font-weight: 700;
            background: var(--border-light);
            padding: 0.15rem 0.35rem;
            border-radius: 4px;
            color: var(--text-muted);
            min-width: 26px;
            text-align: center;
        }}

        .nav-item.active .nav-num {{
            background: var(--accent-blue);
            color: #FFFFFF;
        }}

        /* Main Content Container */
        .content-area {{
            flex: 1;
            min-width: 0;
            padding: 2rem 2.5rem 6rem 2.5rem;
            max-width: 980px;
        }}

        /* Project Metadata Hero Card */
        .project-hero {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.75rem 2rem;
            margin-bottom: 2.5rem;
            box-shadow: var(--card-shadow);
            position: relative;
            overflow: hidden;
        }}

        .project-hero::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #7C3AED, #2563EB, #059669);
        }}

        .interview-pillars-bar {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin-bottom: 1rem;
        }}

        .pillar-pill {{
            font-family: var(--font-ui);
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            background: var(--border-light);
            color: var(--text-secondary);
        }}

        .hero-title-group {{
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }}

        .hero-title {{
            font-family: var(--font-ui);
            font-size: 1.6rem;
            font-weight: 800;
            letter-spacing: -0.6px;
            color: var(--text-main);
        }}

        .hero-subtitle {{
            font-size: 1.05rem;
            color: var(--text-secondary);
            margin-bottom: 1.25rem;
            line-height: 1.6;
        }}

        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            padding-top: 1.25rem;
            border-top: 1px solid var(--border-light);
        }}

        .meta-item {{
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }}

        .meta-label {{
            font-family: var(--font-ui);
            font-size: 0.72rem;
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.8px;
            color: var(--text-muted);
        }}

        .meta-value {{
            font-family: var(--font-ui);
            font-size: 0.92rem;
            font-weight: 600;
            color: var(--text-main);
        }}

        /* Slide Cards */
        .slide-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 2.25rem;
            margin-bottom: 2.5rem;
            box-shadow: var(--card-shadow);
            transition: all 0.2s ease;
            position: relative;
        }}

        .slide-card:hover {{
            box-shadow: var(--card-hover);
            border-color: #CBD5E1;
        }}

        .slide-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding-bottom: 1.25rem;
            border-bottom: 1px solid var(--border-light);
        }}

        .slide-badge-title {{
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }}

        .slide-top-row {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .slide-num-pill {{
            font-family: var(--font-mono);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            background: #0B132B;
            color: #FFFFFF;
            padding: 0.25rem 0.65rem;
            border-radius: 6px;
            display: inline-block;
        }}

        [data-theme="dark"] .slide-num-pill {{
            background: #1E293B;
            color: #38BDF8;
            border: 1px solid #334155;
        }}

        .slide-pillar-tag {{
            font-family: var(--font-ui);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.2rem 0.6rem;
            border-radius: 6px;
            background: var(--accent-purple-bg);
            color: var(--accent-purple);
            border: 1px solid rgba(124, 58, 237, 0.2);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .slide-title-en {{
            font-family: var(--font-ui);
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: -0.3px;
        }}

        .slide-title-bn {{
            font-size: 1rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .slide-actions {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-shrink: 0;
        }}

        .btn-copy {{
            background: var(--bg-body);
            border: 1px solid var(--border);
            color: var(--text-secondary);
            font-family: var(--font-ui);
            font-size: 0.78rem;
            font-weight: 600;
            padding: 0.4rem 0.65rem;
            border-radius: 6px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            transition: all 0.15s ease;
        }}

        .btn-copy:hover {{
            background: var(--border);
            color: var(--text-main);
        }}

        .btn-deck-link {{
            background: var(--accent-blue-bg);
            border: 1px solid rgba(37, 99, 235, 0.2);
            color: var(--accent-blue);
            font-family: var(--font-ui);
            font-size: 0.78rem;
            font-weight: 600;
            padding: 0.4rem 0.65rem;
            border-radius: 6px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            transition: all 0.15s ease;
        }}

        .btn-deck-link:hover {{
            background: var(--accent-blue);
            color: #FFFFFF;
        }}

        /* Objective Box */
        .objective-box {{
            background: var(--bg-body);
            border-left: 3px solid var(--accent-blue);
            padding: 0.85rem 1.15rem;
            border-radius: 0 8px 8px 0;
            margin-bottom: 1.5rem;
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.6;
        }}

        .objective-label {{
            font-family: var(--font-ui);
            font-weight: 700;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--accent-blue);
            margin-bottom: 0.25rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        /* Speech Presentation Box */
        .speech-section {{
            margin-bottom: 1.75rem;
        }}

        .speech-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.75rem;
        }}

        .speech-label {{
            font-family: var(--font-ui);
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .speech-box {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1.5rem 1.75rem;
            font-size: 1.08rem;
            line-height: 1.85;
            color: var(--text-main);
            position: relative;
        }}

        .speech-box p {{
            margin-bottom: 1rem;
        }}

        .speech-box p:last-child {{
            margin-bottom: 0;
        }}

        .tech-inline {{
            font-family: var(--font-mono);
            font-size: 0.9em;
            font-weight: 600;
            background: var(--border-light);
            color: var(--navy-primary);
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
            border: 1px solid rgba(0, 0, 0, 0.05);
            display: inline-block;
        }}

        [data-theme="dark"] .tech-inline {{
            background: #1E293B;
            color: #38BDF8;
            border-color: #334155;
        }}

        /* Engineering Knowledge Depth Section */
        .engineering-depth {{
            border-top: 1px dashed var(--border);
            padding-top: 1.25rem;
            margin-top: 1.25rem;
        }}

        .engineering-label {{
            font-family: var(--font-ui);
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--text-muted);
            margin-bottom: 0.85rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .tech-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 0.75rem;
        }}

        .tech-card {{
            background: var(--bg-body);
            border: 1px solid var(--border-light);
            border-radius: 8px;
            padding: 0.75rem 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
        }}

        .tech-card-label {{
            font-family: var(--font-ui);
            font-size: 0.72rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .tech-card-val {{
            font-family: var(--font-mono);
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-main);
            word-break: break-word;
        }}

        /* Technical Cheat Sheet Section */
        .cheat-sheet-section {{
            margin-top: 3.5rem;
            padding-top: 2.5rem;
            border-top: 2px solid var(--border);
        }}

        .section-header-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--accent-amber-bg);
            color: var(--accent-amber);
            font-family: var(--font-ui);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.3rem 0.75rem;
            border-radius: 9999px;
            margin-bottom: 0.75rem;
            border: 1px solid rgba(217, 119, 6, 0.25);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .section-main-title {{
            font-family: var(--font-ui);
            font-size: 1.5rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            color: var(--text-main);
            margin-bottom: 0.5rem;
        }}

        .section-subtext {{
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }}

        .qa-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.75rem 2rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--card-shadow);
        }}

        .qa-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 1rem;
        }}

        .qa-q {{
            font-family: var(--font-bn);
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-main);
            line-height: 1.45;
        }}

        .qa-ans {{
            font-size: 1.05rem;
            line-height: 1.8;
            color: var(--text-secondary);
            background: var(--bg-body);
            border-radius: 8px;
            padding: 1.25rem 1.5rem;
            border-left: 3px solid var(--accent-green);
        }}

        /* Toast notification */
        .toast {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #0B132B;
            color: #FFFFFF;
            font-family: var(--font-ui);
            font-size: 0.85rem;
            font-weight: 600;
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            opacity: 0;
            transform: translateY(10px);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            pointer-events: none;
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Progress Bar */
        .scroll-progress {{
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, #7C3AED, #2563EB, #059669);
            width: 0%;
            z-index: 101;
            transition: width 0.1s ease;
        }}

        /* Responsive Breakpoints */
        @media (max-width: 1024px) {{
            .sidebar {{
                display: none;
            }}
            .content-area {{
                padding: 1.5rem;
                max-width: 100%;
            }}
            .search-box input {{
                width: 150px;
            }}
            .search-box input:focus {{
                width: 200px;
            }}
        }}

        @media (max-width: 640px) {{
            .site-header {{
                padding: 0.6rem 1rem;
            }}
            .brand-text h1 span {{
                display: none;
            }}
            .search-box {{
                display: none;
            }}
            .slide-card {{
                padding: 1.5rem 1.25rem;
            }}
            .slide-header {{
                flex-direction: column;
            }}
            .speech-box {{
                font-size: 1rem;
                padding: 1.25rem;
            }}
        }}

        /* Print Optimization */
        @media print {{
            .site-header, .sidebar, .slide-actions, .btn-ctrl, .scroll-progress {{
                display: none !important;
            }}
            .content-area {{
                padding: 0;
                max-width: 100%;
            }}
            .slide-card {{
                page-break-inside: avoid;
                border: 1px solid #ccc;
                box-shadow: none;
                margin-bottom: 2rem;
            }}
        }}
    </style>
</head>
<body>

    <div class="scroll-progress" id="progressBar"></div>

    <!-- Header -->
    <header class="site-header">
        <div class="brand-area">
            <div class="brand-logo">AX</div>
            <div class="brand-text">
                <h1>AutoTaskX <span>· Interview Engineering Guide</span></h1>
            </div>
            <span class="badge-role">Digital Twin &amp; Data Engineer</span>
            <span class="badge-live">Live Production 24/7</span>
        </div>

        <div class="header-controls">
            <div class="search-box">
                <svg class="search-icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
                <input type="text" id="searchInput" placeholder="Search slides, pillars, tech...">
            </div>
            <button class="btn-ctrl" id="themeToggle" title="Toggle Dark/Light Mode">🌙 Theme</button>
            <button class="btn-ctrl" id="fontInc" title="Increase Font Size">A+</button>
            <button class="btn-ctrl" id="fontDec" title="Decrease Font Size">A-</button>
            <a href="#cheat-sheet" class="btn-ctrl">⚡ Q&amp;A</a>
            <a href="index.html" target="_blank" class="btn-ctrl btn-deck">🖥️ Open Slides Deck ↗</a>
        </div>
    </header>

    <div class="app-container">
        <!-- Sidebar Navigation -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-heading">Interview Pillars &amp; Slides</div>
"""

for s in slides:
    html_content += f"""            <a href="#slide-{s['num']}" class="nav-item" data-slide="{s['num']}">
                <span class="nav-num">{s['num']}</span>
                <span>{s['en_title'][:28]}</span>
            </a>\n"""

html_content += """            <div class="sidebar-heading">Interview Cheat Sheet</div>
            <a href="#cheat-sheet" class="nav-item" data-slide="cheat">
                <span class="nav-num">⚡</span>
                <span>Technical Interview Q&amp;A</span>
            </a>
        </aside>

        <!-- Main Content -->
        <main class="content-area">
            <!-- Executive Project Context Card -->
            <section class="project-hero">
                <div class="interview-pillars-bar">
                    <span class="pillar-pill">1. Objectives</span>
                    <span class="pillar-pill">2. Technical Approach</span>
                    <span class="pillar-pill">3. Individual Contributions</span>
                    <span class="pillar-pill">4. Key Challenges</span>
                    <span class="pillar-pill">5. Solutions</span>
                    <span class="pillar-pill">6. Outcomes &amp; Impact</span>
                </div>
                <div class="hero-title-group">
                    <h2 class="hero-title">AutoTaskX — Digital Twin &amp; Data Engineer Guide</h2>
                    <span class="badge-live">Client Project · Active 24/7</span>
                </div>
                <p class="hero-subtitle">
                    বাংলাদেশের একটি বড় টেক্সটাইল ফ্যাক্টরিতে ৪ মাসে তৈরি ও লাইভ (Live) করা Industrial IoT (ইন্ডাস্ট্রিয়াল আই-ও-টি),
                    MQTT (এম-কিউ-টি-টি), AI Automation (এ-আই অটোমেশন) এবং Real-time Digital Twin (রিয়েল-টাইম ডিজিটাল টুইন) প্ল্যাটফর্ম।
                </p>

                <div class="meta-grid">
                    <div class="meta-item">
                        <span class="meta-label">Target Role</span>
                        <span class="meta-value">Digital Twin &amp; Data Engineer</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Candidate</span>
                        <span class="meta-value">Sheikh Shamiul Shakib (BUBT · CSE)</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Timeline &amp; Status</span>
                        <span class="meta-value">4 Months · 100% Active Production 24/7</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Core Tech Stack</span>
                        <span class="meta-value">Digital Twin · EMQX MQTT · FastAPI · TimescaleDB · AI Vision</span>
                    </div>
                </div>
            </section>

            <!-- Slide by Slide Cards -->
"""

for s in slides:
    formatted_speech = format_speech(s['speech'])
    
    html_content += f"""
            <article class="slide-card" id="slide-{s['num']}" data-search="{html.escape(s['raw_title'])} {html.escape(s['pillar'])} {html.escape(s['objective'])} {html.escape(s['speech'][:200])}">
                <div class="slide-header">
                    <div class="slide-badge-title">
                        <div class="slide-top-row">
                            <span class="slide-num-pill">SLIDE {s['num']}</span>
                            <span class="slide-pillar-tag">{html.escape(s['pillar'])}</span>
                        </div>
                        <h3 class="slide-title-en">{html.escape(s['en_title'])}</h3>
                        {f'<div class="slide-title-bn">{html.escape(s["bn_title"])}</div>' if s['bn_title'] else ''}
                    </div>
                    <div class="slide-actions">
                        <button class="btn-copy" onclick="copySpeech('speech-text-{s['num']}', this)">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                            Copy Speech
                        </button>
                        <a href="index.html#slide-{int(s['num'])}" target="_blank" class="btn-deck-link">
                            View Deck ↗
                        </a>
                    </div>
                </div>

                <div class="objective-box">
                    <div class="objective-label">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="12 8 8 12 12 16 12 8"></polygon></svg>
                        স্লাইডের মূল লক্ষ্য (Slide Objective)
                    </div>
                    {html.escape(s['objective'])}
                </div>

                <div class="speech-section">
                    <div class="speech-header">
                        <div class="speech-label">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                            English Spoken Script (With Bangla Pronunciation)
                        </div>
                    </div>
                    <div class="speech-box" id="speech-text-{s['num']}">
                        {formatted_speech}
                    </div>
                </div>

                <div class="engineering-depth">
                    <div class="engineering-label">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                        Advanced Engineering Knowledge &amp; System Specs
                    </div>
                    <div class="tech-grid">
"""
    for tp in s['tech_points']:
        html_content += f"""                        <div class="tech-card">
                            <span class="tech-card-label">{html.escape(tp['label'])}</span>
                            <span class="tech-card-val">{html.escape(tp['val'])}</span>
                        </div>\n"""
    html_content += """                    </div>
                </div>
            </article>
"""

# Technical Cheat Sheet Section
html_content += """
            <!-- Technical Q&A Section -->
            <section class="cheat-sheet-section" id="cheat-sheet">
                <span class="section-header-badge">Interview Panel Master Cheat Sheet</span>
                <h2 class="section-main-title">6 Key Technical Questions &amp; Fluent English Answers</h2>
                <p class="section-subtext">Easy-to-read international English answers for Digital Twin &amp; Data Engineer interviews (with Bangla pronunciation for tricky words).</p>
"""

for cq in cheat_questions:
    html_content += f"""
                <div class="qa-card">
                    <div class="qa-header">
                        <div class="qa-q">প্রশ্ন {cq['num']}: &ldquo;{html.escape(cq['title'])}&rdquo;</div>
                        <button class="btn-copy" onclick="copyText(`{html.escape(cq['answer']).replace(chr(10), ' ')}`, this)">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                            Copy Answer
                        </button>
                    </div>
                    <div class="qa-ans">
                        <strong>স্মার্ট উত্তর:</strong><br>
                        &ldquo;{html.escape(cq['answer'])}&rdquo;
                    </div>
                </div>
"""

html_content += """
            </section>
        </main>
    </div>

    <!-- Toast Component -->
    <div class="toast" id="toastBox">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
        <span id="toastMsg">ক্লিপবোর্ডে কপি সম্পন্ন হয়েছে!</span>
    </div>

    <script>
        function copySpeech(elementId, btn) {
            const el = document.getElementById(elementId);
            if (!el) return;
            const text = el.innerText;
            navigator.clipboard.writeText(text).then(() => {
                showToast("স্পিচ টেক্সট ক্লিপবোর্ডে কপি হয়েছে!");
                const originalText = btn.innerHTML;
                btn.innerHTML = `✓ Copied!`;
                btn.style.color = '#059669';
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.color = '';
                }, 2000);
            });
        }

        function copyText(text, btn) {
            navigator.clipboard.writeText(text).then(() => {
                showToast("উত্তরটি ক্লিপবোর্ডে কপি হয়েছে!");
                const originalText = btn.innerHTML;
                btn.innerHTML = `✓ Copied!`;
                btn.style.color = '#059669';
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.color = '';
                }, 2000);
            });
        }

        function showToast(msg) {
            const toast = document.getElementById('toastBox');
            const toastMsg = document.getElementById('toastMsg');
            toastMsg.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 2500);
        }

        const searchInput = document.getElementById('searchInput');
        const slideCards = document.querySelectorAll('.slide-card');

        searchInput.addEventListener('input', (e) => {
            const q = e.target.value.toLowerCase().trim();
            slideCards.forEach(card => {
                const searchData = card.getAttribute('data-search').toLowerCase();
                const textContent = card.innerText.toLowerCase();
                if (!q || searchData.includes(q) || textContent.includes(q)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        });

        window.addEventListener('scroll', () => {
            const winScroll = document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById('progressBar').style.width = scrolled + '%';
        });

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    const navItems = document.querySelectorAll('.sidebar .nav-item');
                    navItems.forEach(item => {
                        if (item.getAttribute('href') === '#' + id) {
                            item.classList.add('active');
                            item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
                        } else {
                            item.classList.remove('active');
                        }
                    });
                }
            });
        }, { threshold: 0.25 });

        document.querySelectorAll('.slide-card, .cheat-sheet-section').forEach(section => {
            observer.observe(section);
        });

        const themeBtn = document.getElementById('themeToggle');
        const currentTheme = localStorage.getItem('ax_guide_theme') || 'light';
        if (currentTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeBtn.innerText = '☀️ Light';
        }

        themeBtn.addEventListener('click', () => {
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {
                document.documentElement.removeAttribute('data-theme');
                themeBtn.innerText = '🌙 Dark';
                localStorage.setItem('ax_guide_theme', 'light');
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                themeBtn.innerText = '☀️ Light';
                localStorage.setItem('ax_guide_theme', 'dark');
            }
        });

        let currentFontSize = 16;
        document.getElementById('fontInc').addEventListener('click', () => {
            if (currentFontSize < 22) {
                currentFontSize += 1;
                document.documentElement.style.setProperty('--base-font-size', currentFontSize + 'px');
            }
        });

        document.getElementById('fontDec').addEventListener('click', () => {
            if (currentFontSize > 13) {
                currentFontSize -= 1;
                document.documentElement.style.setProperty('--base-font-size', currentFontSize + 'px');
            }
        });

        window.addEventListener('keydown', (e) => {
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            if (e.key === 'j' || e.key === 'ArrowDown') {
                const active = document.querySelector('.sidebar .nav-item.active');
                if (active && active.nextElementSibling && active.nextElementSibling.classList.contains('nav-item')) {
                    active.nextElementSibling.click();
                }
            } else if (e.key === 'k' || e.key === 'ArrowUp') {
                const active = document.querySelector('.sidebar .nav-item.active');
                if (active && active.previousElementSibling && active.previousElementSibling.classList.contains('nav-item')) {
                    active.previousElementSibling.click();
                }
            }
        });
    </script>
</body>
</html>
"""

with open('guide.html', 'w', encoding='utf-8') as out_f:
    out_f.write(html_content)

print(f"Generated guide.html successfully. Size: {len(html_content)} bytes.")
