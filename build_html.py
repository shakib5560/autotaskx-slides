import json
import html
import re

with open('guide_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

slides = data['slides']
cheat_questions = data['cheat_questions']

TECH_KEYWORDS = [
    'FastAPI', 'MQTT', 'TimescaleDB', 'PostgreSQL', 'Postgres', 'AWS S3', 'S3',
    'CoaXPress', 'Basler', 'Kubelka-Munk', 'Digital Twin', 'EMQX', 'WebSocket',
    'WebSockets', 'Next.js', 'OpenCV', 'YOLO', 'Modbus', 'Modbus RTU/TCP', 'OPC-UA',
    'RS-485', 'PT100', 'Pre-signed S3 URL', 'Pre-signed URL', 'Pre-signed',
    'Right-First-Time', 'RFT', 'OEE', 'ΔE', 'Delta-E', 'FIFO', 'AsyncIO', 'ASGI', 'WSGI',
    'SAP', 'ERP', 'AI Automation', 'Data Pipeline', 'Data Engineering', 'Edge Gateway',
    'Hypertable', 'Hypertables', 'Predictive Maintenance', 'Textile OS', 'Datatex NOW',
    'Datatex', 'Infor M3', 'Closed-Loop Control'
]
ORDERED_KWS = sorted(set(TECH_KEYWORDS), key=len, reverse=True)
KW_PATTERN = re.compile(r'(?<![\w\-])(' + '|'.join(re.escape(k) for k in ORDERED_KWS) + r')(?![\w\-])')
BN_PRON_PATTERN = re.compile(r'(\([^\)]*[\u0980-\u09ff][^\)]*\))')


def highlight_inline_tokens(escaped_text):
    """Wrap Bengali pronunciation cues and technical keywords without nesting HTML tags."""
    # 1) Wrap Bengali pronunciation parentheses first
    text = BN_PRON_PATTERN.sub(r'<span class="bn-pron">\1</span>', escaped_text)
    # 2) Highlight tech keywords only in text segments outside HTML tags
    parts = re.split(r'(<[^>]+>)', text)
    for i in range(0, len(parts), 2):
        parts[i] = KW_PATTERN.sub(r'<span class="tech-inline">\1</span>', parts[i])
    return ''.join(parts)


def format_speech(text):
    """Format spoken monologue paragraphs with mobile-scannable cue headers and pronunciation styling."""
    escaped = html.escape(text)
    paragraphs = [p.strip() for p in escaped.split('\n\n') if p.strip()]
    out = []
    for p in paragraphs:
        lines = [ln.strip() for ln in p.split('\n') if ln.strip()]
        if lines and lines[0].startswith('▶'):
            cue_line = highlight_inline_tokens(lines[0])
            lower_cue = lines[0].lower()
            cue_cls = 'cue-info'
            if 'problem' in lower_cue or 'faced' in lower_cue or 'challenge' in lower_cue:
                cue_cls = 'cue-problem'
            elif 'solution' in lower_cue or 'discovery' in lower_cue or 'wanted' in lower_cue or 'goal' in lower_cue:
                cue_cls = 'cue-solution'
            elif 'result' in lower_cue or 'asked' in lower_cue:
                cue_cls = 'cue-result'
            body_html = '<br>'.join(highlight_inline_tokens(ln) for ln in lines[1:])
            out.append(f'<div class="cue-block {cue_cls}"><div class="cue-heading">{cue_line}</div>')
            if body_html:
                out.append(f'<p>{body_html}</p>')
            out.append('</div>')
        else:
            body_html = '<br>'.join(highlight_inline_tokens(ln) for ln in lines)
            out.append(f'<p>{body_html}</p>')
    return '\n'.join(out)


def format_answer(text):
    """Format Q&A answers with pronunciation cues and highlighted tech terms."""
    escaped = html.escape(text)
    lines = [ln.strip() for ln in escaped.split('\n') if ln.strip()]
    return '<br>'.join(highlight_inline_tokens(ln) for ln in lines)


html_content = f"""<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
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
            --bg-header: rgba(255, 255, 255, 0.96);
            --border: #E2E5DF;
            --border-light: #EDF0EB;
            --text-main: #141816;
            --text-secondary: #3F4742;
            --text-muted: #6E7872;
            --pron-text: #64748B;
            --navy-primary: #0B132B;
            --navy-surface: #1C2541;
            --accent-blue: #2563EB;
            --accent-blue-bg: #EFF6FF;
            --accent-green: #059669;
            --accent-green-bg: #ECFDF5;
            --accent-amber: #D97706;
            --accent-amber-bg: #FFFBEB;
            --accent-red: #DC2626;
            --accent-red-bg: #FEF2F2;
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
            --bg-header: rgba(11, 18, 32, 0.96);
            --border: #1F2A3F;
            --border-light: #162032;
            --text-main: #F1F5F9;
            --text-secondary: #CBD5E1;
            --text-muted: #94A3B8;
            --pron-text: #94A3B8;
            --navy-primary: #38BDF8;
            --navy-surface: #1E293B;
            --accent-blue: #60A5FA;
            --accent-blue-bg: #172554;
            --accent-green: #34D399;
            --accent-green-bg: #064E3B;
            --accent-amber: #FBBF24;
            --accent-amber-bg: #451A03;
            --accent-red: #F87171;
            --accent-red-bg: #450A0A;
            --accent-purple: #A78BFA;
            --accent-purple-bg: #2E1065;
            --card-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
            --card-hover: 0 8px 28px rgba(0, 0, 0, 0.45);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
        }}

        html {{
            font-size: var(--base-font-size);
            scroll-behavior: smooth;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: var(--font-ui);
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
            transition: background-color 0.25s ease, color 0.25s ease;
        }}

        body.drawer-open {{
            overflow: hidden;
        }}

        /* Header Bar */
        .site-header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--bg-header);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
            padding: 0.7rem 1.25rem;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 0.65rem 1rem;
        }}

        .header-top-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.75rem;
            width: 100%;
        }}

        .brand-area {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
            min-width: 0;
        }}

        .brand-logo {{
            width: 32px;
            height: 32px;
            flex-shrink: 0;
            background: #0B132B;
            color: #38BDF8;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-ui);
            font-weight: 800;
            font-size: 0.92rem;
            letter-spacing: -0.5px;
            box-shadow: 0 2px 6px rgba(11, 19, 43, 0.3);
        }}

        .brand-text h1 {{
            font-family: var(--font-ui);
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: -0.3px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 0.4rem;
            white-space: nowrap;
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
            white-space: nowrap;
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
            white-space: nowrap;
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
            gap: 0.45rem;
            flex-wrap: wrap;
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
            font-size: 0.88rem;
            padding: 0.48rem 2rem 0.48rem 2.1rem;
            border-radius: 8px;
            width: 220px;
            min-height: 36px;
            transition: all 0.2s ease;
        }}

        .search-box input:focus {{
            outline: none;
            border-color: var(--accent-blue);
            width: 260px;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
        }}

        .search-icon {{
            position: absolute;
            left: 0.7rem;
            width: 15px;
            height: 15px;
            fill: none;
            stroke: var(--text-muted);
            stroke-width: 2;
            pointer-events: none;
        }}

        .search-clear {{
            position: absolute;
            right: 0.45rem;
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 0.85rem;
            cursor: pointer;
            padding: 0.2rem 0.35rem;
            display: none;
        }}

        .search-clear.visible {{
            display: inline-flex;
        }}

        .btn-ctrl {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-secondary);
            font-family: var(--font-ui);
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.4rem 0.65rem;
            min-height: 36px;
            border-radius: 8px;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.32rem;
            transition: all 0.15s ease;
            text-decoration: none;
            white-space: nowrap;
        }}

        .btn-ctrl:hover {{
            background: var(--border-light);
            color: var(--text-main);
            border-color: var(--text-muted);
        }}

        .btn-ctrl.active-state {{
            background: var(--accent-blue-bg);
            color: var(--accent-blue);
            border-color: var(--accent-blue);
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

        .mobile-only {{
            display: none;
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
            width: 310px;
            flex-shrink: 0;
            position: sticky;
            top: 58px;
            height: calc(100vh - 58px);
            overflow-y: auto;
            padding: 1.25rem 1rem 3rem 1.25rem;
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
            flex-shrink: 0;
        }}

        .nav-item.active .nav-num {{
            background: var(--accent-blue);
            color: #FFFFFF;
        }}

        /* Mobile Slide Jump Drawer */
        .drawer-backdrop {{
            position: fixed;
            inset: 0;
            background: rgba(8, 12, 20, 0.58);
            backdrop-filter: blur(4px);
            z-index: 250;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.2s ease;
        }}

        .drawer-backdrop.open {{
            opacity: 1;
            pointer-events: auto;
        }}

        .mobile-drawer {{
            position: fixed;
            left: 0;
            right: 0;
            bottom: 0;
            max-height: 82vh;
            background: var(--bg-card);
            border-top: 1px solid var(--border);
            border-radius: 18px 18px 0 0;
            box-shadow: 0 -12px 40px rgba(0, 0, 0, 0.25);
            z-index: 260;
            transform: translateY(105%);
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
            padding-bottom: env(safe-area-inset-bottom);
        }}

        .mobile-drawer.open {{
            transform: translateY(0);
        }}

        .mobile-drawer-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 1.15rem 0.75rem;
            border-bottom: 1px solid var(--border);
        }}

        .mobile-drawer-header h3 {{
            font-size: 0.98rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .mobile-drawer-list {{
            overflow-y: auto;
            padding: 0.65rem 0.85rem 1.25rem;
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }}

        .mobile-drawer-item {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.72rem 0.85rem;
            border-radius: 10px;
            text-decoration: none;
            color: var(--text-main);
            background: var(--bg-body);
            border: 1px solid var(--border-light);
            min-height: 46px;
        }}

        .mobile-drawer-item.active {{
            background: var(--accent-blue-bg);
            border-color: var(--accent-blue);
            color: var(--accent-blue);
        }}

        .mobile-drawer-titles {{
            display: flex;
            flex-direction: column;
            min-width: 0;
        }}

        .mobile-drawer-en {{
            font-size: 0.88rem;
            font-weight: 600;
            line-height: 1.3;
        }}

        .mobile-drawer-bn {{
            font-size: 0.78rem;
            color: var(--text-muted);
            line-height: 1.3;
        }}

        /* Main Content Container */
        .content-area {{
            flex: 1;
            min-width: 0;
            padding: 2rem 2.25rem 6rem 2.25rem;
            max-width: 960px;
        }}

        /* Project Metadata Hero Card */
        .project-hero {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1.6rem 1.85rem;
            margin-bottom: 2rem;
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
            gap: 0.45rem;
            flex-wrap: wrap;
            margin-bottom: 0.9rem;
        }}

        .pillar-pill {{
            font-family: var(--font-ui);
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.22rem 0.55rem;
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
            font-size: 1.48rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            color: var(--text-main);
        }}

        .hero-subtitle {{
            font-size: 0.98rem;
            color: var(--text-secondary);
            margin-bottom: 1.15rem;
            line-height: 1.65;
        }}

        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr));
            gap: 0.9rem;
            padding-top: 1.1rem;
            border-top: 1px solid var(--border-light);
        }}

        .meta-item {{
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
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
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-main);
        }}

        /* Slide Cards */
        .slide-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: var(--card-shadow);
            transition: box-shadow 0.2s ease, border-color 0.2s ease;
            position: relative;
            scroll-margin-top: 84px;
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
            margin-bottom: 1.25rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border-light);
        }}

        .slide-badge-title {{
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            min-width: 0;
        }}

        .slide-top-row {{
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.45rem;
        }}

        .slide-num-pill {{
            font-family: var(--font-mono);
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            background: #0B132B;
            color: #FFFFFF;
            padding: 0.24rem 0.6rem;
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
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.2rem 0.55rem;
            border-radius: 6px;
            background: var(--accent-purple-bg);
            color: var(--accent-purple);
            border: 1px solid rgba(124, 58, 237, 0.2);
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }}

        .slide-title-en {{
            font-family: var(--font-ui);
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-main);
            letter-spacing: -0.3px;
            line-height: 1.35;
        }}

        .slide-title-bn {{
            font-size: 0.95rem;
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
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.45rem 0.7rem;
            min-height: 36px;
            border-radius: 8px;
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
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.45rem 0.7rem;
            min-height: 36px;
            border-radius: 8px;
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
            padding: 0.85rem 1.05rem;
            border-radius: 0 8px 8px 0;
            margin-bottom: 1.25rem;
            font-size: 0.94rem;
            color: var(--text-secondary);
            line-height: 1.65;
        }}

        .objective-label {{
            font-family: var(--font-ui);
            font-weight: 700;
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.7px;
            color: var(--accent-blue);
            margin-bottom: 0.25rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        /* Speech Presentation Box */
        .speech-section {{
            margin-bottom: 1.5rem;
        }}

        .speech-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.65rem;
        }}

        .speech-label {{
            font-family: var(--font-ui);
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.7px;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .speech-box {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 1.4rem 1.55rem;
            font-size: 1.08rem;
            line-height: 1.92;
            color: var(--text-main);
            position: relative;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }}

        .speech-box p {{
            margin-bottom: 1rem;
        }}

        .speech-box p:last-child {{
            margin-bottom: 0;
        }}

        /* Visual Problem -> Solution -> Result Cue Blocks */
        .cue-block {{
            margin: 1.1rem 0;
            padding: 0.85rem 1rem;
            border-radius: 10px;
            border-left: 3.5px solid var(--accent-blue);
            background: var(--bg-body);
        }}

        .cue-block.cue-problem {{
            border-left-color: var(--accent-red);
            background: var(--accent-red-bg);
        }}

        .cue-block.cue-solution {{
            border-left-color: var(--accent-blue);
            background: var(--accent-blue-bg);
        }}

        .cue-block.cue-result {{
            border-left-color: var(--accent-green);
            background: var(--accent-green-bg);
        }}

        .cue-heading {{
            font-weight: 700;
            font-size: 0.94rem;
            margin-bottom: 0.35rem;
            color: var(--text-main);
        }}

        /* Soft inline Bengali pronunciation cue */
        .bn-pron {{
            font-family: 'Hind Siliguri', var(--font-ui);
            font-size: 0.86em;
            font-weight: 500;
            color: var(--pron-text);
            padding: 0 0.12rem;
        }}

        body.hide-pron .bn-pron {{
            display: none;
        }}

        .tech-inline {{
            font-family: var(--font-mono);
            font-size: 0.88em;
            font-weight: 600;
            background: var(--border-light);
            color: var(--navy-primary);
            padding: 0.08rem 0.36rem;
            border-radius: 4px;
            border: 1px solid rgba(0, 0, 0, 0.06);
        }}

        [data-theme="dark"] .tech-inline {{
            background: #1E293B;
            color: #38BDF8;
            border-color: #334155;
        }}

        /* Engineering Knowledge Depth Section */
        .engineering-depth {{
            border-top: 1px dashed var(--border);
            padding-top: 1.15rem;
            margin-top: 1.15rem;
        }}

        .engineering-label {{
            font-family: var(--font-ui);
            font-size: 0.74rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--text-muted);
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .tech-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
            gap: 0.7rem;
        }}

        .tech-card {{
            background: var(--bg-body);
            border: 1px solid var(--border-light);
            border-radius: 8px;
            padding: 0.75rem 0.95rem;
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
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 2px solid var(--border);
            scroll-margin-top: 84px;
        }}

        .section-header-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            background: var(--accent-amber-bg);
            color: var(--accent-amber);
            font-family: var(--font-ui);
            font-size: 0.74rem;
            font-weight: 700;
            padding: 0.28rem 0.75rem;
            border-radius: 9999px;
            margin-bottom: 0.7rem;
            border: 1px solid rgba(217, 119, 6, 0.25);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .section-main-title {{
            font-family: var(--font-ui);
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: -0.4px;
            color: var(--text-main);
            margin-bottom: 0.45rem;
        }}

        .section-subtext {{
            font-size: 0.96rem;
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
        }}

        .qa-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--card-shadow);
        }}

        .qa-header {{
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 0.85rem;
            margin-bottom: 0.9rem;
        }}

        .qa-q {{
            font-family: var(--font-ui);
            font-size: 1.08rem;
            font-weight: 700;
            color: var(--text-main);
            line-height: 1.48;
        }}

        .qa-ans {{
            font-size: 1.04rem;
            line-height: 1.88;
            color: var(--text-main);
            background: var(--bg-body);
            border-radius: 8px;
            padding: 1.15rem 1.3rem;
            border-left: 3px solid var(--accent-green);
        }}

        /* Single-Slide Focus Mode */
        body.focus-mode .project-hero {{
            display: none;
        }}

        body.focus-mode .slide-card,
        body.focus-mode .cheat-sheet-section {{
            display: none;
        }}

        body.focus-mode .slide-card.focus-active,
        body.focus-mode .cheat-sheet-section.focus-active {{
            display: block;
            margin-top: 0;
            padding-top: 0;
            border-top: none;
        }}

        /* Sticky Mobile Bottom Reading Bar */
        .mobile-bottom-nav {{
            display: none;
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
            padding: 0.72rem 1.15rem;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
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
            .mobile-only {{
                display: inline-flex;
            }}
            .content-area {{
                padding: 1.25rem 1.25rem 6rem 1.25rem;
                max-width: 100%;
            }}
            .mobile-bottom-nav {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 0.5rem;
                position: fixed;
                left: 0;
                right: 0;
                bottom: 0;
                z-index: 150;
                background: var(--bg-header);
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                border-top: 1px solid var(--border);
                padding: 0.55rem 0.85rem calc(0.55rem + env(safe-area-inset-bottom));
                box-shadow: 0 -6px 20px rgba(0, 0, 0, 0.08);
            }}
            .mnav-btn {{
                background: var(--bg-card);
                border: 1px solid var(--border);
                color: var(--text-main);
                font-family: var(--font-ui);
                font-size: 0.86rem;
                font-weight: 700;
                padding: 0.55rem 0.9rem;
                min-height: 42px;
                border-radius: 10px;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 0.35rem;
            }}
            .mnav-btn:disabled {{
                opacity: 0.4;
                cursor: default;
            }}
            .mnav-jump {{
                flex: 1;
                background: var(--accent-blue-bg);
                border: 1px solid rgba(37, 99, 235, 0.25);
                color: var(--accent-blue);
                font-family: var(--font-mono);
                font-size: 0.84rem;
                font-weight: 700;
                min-height: 42px;
                border-radius: 10px;
                cursor: pointer;
                padding: 0.45rem 0.75rem;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }}
            .toast {{
                bottom: 76px;
                left: 50%;
                right: auto;
                transform: translateX(-50%) translateY(10px);
                white-space: nowrap;
            }}
            .toast.show {{
                transform: translateX(-50%) translateY(0);
            }}
        }}

        @media (max-width: 768px) {{
            .site-header {{
                padding: 0.55rem 0.75rem;
                gap: 0.5rem;
            }}
            .brand-text h1 span,
            .badge-role,
            .badge-live {{
                display: none;
            }}
            .header-controls {{
                gap: 0.35rem;
            }}
            .btn-ctrl {{
                padding: 0.38rem 0.55rem;
                font-size: 0.76rem;
                min-height: 36px;
            }}
            .btn-ctrl .btn-label-desktop {{
                display: none;
            }}
            .search-box {{
                order: 3;
                width: 100%;
            }}
            .search-box input,
            .search-box input:focus {{
                width: 100%;
                font-size: 0.92rem;
            }}
            .content-area {{
                padding: 0.85rem 0.7rem 5.75rem 0.7rem;
            }}
            .project-hero {{
                padding: 1.1rem 0.95rem;
                margin-bottom: 1rem;
                border-radius: 12px;
            }}
            .hero-title {{
                font-size: 1.2rem;
            }}
            .hero-subtitle {{
                font-size: 0.92rem;
            }}
            .slide-card {{
                padding: 1.1rem 0.95rem;
                margin-bottom: 1.15rem;
                border-radius: 12px;
                scroll-margin-top: 118px;
            }}
            .cheat-sheet-section {{
                scroll-margin-top: 118px;
            }}
            .slide-header {{
                flex-direction: column;
                gap: 0.7rem;
                margin-bottom: 0.95rem;
                padding-bottom: 0.85rem;
            }}
            .slide-title-en {{
                font-size: 1.12rem;
            }}
            .slide-actions {{
                width: 100%;
            }}
            .slide-actions .btn-copy,
            .slide-actions .btn-deck-link {{
                flex: 1;
                justify-content: center;
                min-height: 40px;
                font-size: 0.82rem;
            }}
            .speech-box {{
                font-size: 1.06rem;
                line-height: 1.92;
                padding: 1rem 0.95rem;
            }}
            .cue-block {{
                padding: 0.78rem 0.85rem;
                margin: 0.9rem 0;
            }}
            .qa-card {{
                padding: 1.1rem 0.95rem;
            }}
            .qa-header {{
                flex-direction: column;
                align-items: stretch;
                gap: 0.65rem;
            }}
            .qa-header .btn-copy {{
                align-self: flex-start;
                min-height: 38px;
            }}
            .qa-ans {{
                padding: 0.95rem;
                font-size: 1.03rem;
                line-height: 1.88;
            }}
        }}

        /* Print Optimization */
        @media print {{
            .site-header, .sidebar, .slide-actions, .btn-ctrl, .scroll-progress, .mobile-bottom-nav, .mobile-drawer, .drawer-backdrop {{
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
        <div class="header-top-row">
            <div class="brand-area">
                <div class="brand-logo">AX</div>
                <div class="brand-text">
                    <h1>AutoTaskX <span>· Engineering Guide</span></h1>
                </div>
                <span class="badge-role">Digital Twin &amp; Data Engineer</span>
                <span class="badge-live">Live 24/7</span>
            </div>

            <div class="header-controls">
                <button class="btn-ctrl mobile-only" id="openDrawerBtn" title="Jump to Slide">📑 <span class="btn-label-desktop">Slides</span></button>
                <button class="btn-ctrl" id="focusToggle" title="Read one slide at a time">🎯 Focus</button>
                <button class="btn-ctrl active-state" id="pronToggle" title="Show/Hide Bengali Pronunciation">উচ্চারণ</button>
                <button class="btn-ctrl" id="fontDec" title="Decrease Font Size">A-</button>
                <button class="btn-ctrl" id="fontInc" title="Increase Font Size">A+</button>
                <button class="btn-ctrl" id="themeToggle" title="Toggle Dark/Light Mode">🌙</button>
                <a href="index.html" target="_blank" class="btn-ctrl btn-deck">🖥️ <span class="btn-label-desktop">Slides Deck</span></a>
            </div>
        </div>

        <div class="search-box">
            <svg class="search-icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="search" id="searchInput" placeholder="Search slides, MQTT, Digital Twin, Q&A...">
            <button type="button" class="search-clear" id="searchClear" aria-label="Clear search">✕</button>
        </div>
    </header>

    <div class="app-container">
        <!-- Desktop Sidebar Navigation -->
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-heading">Slides (01 – 18)</div>
"""

for s in slides:
    html_content += f"""            <a href="#slide-{s['num']}" class="nav-item" data-slide="{s['num']}">
                <span class="nav-num">{s['num']}</span>
                <span>{html.escape(s['en_title'][:30])}</span>
            </a>\n"""

html_content += """            <div class="sidebar-heading">Interview Cheat Sheet</div>
            <a href="#cheat-sheet" class="nav-item" data-slide="cheat">
                <span class="nav-num">⚡</span>
                <span>6 Key Questions &amp; Answers</span>
            </a>
        </aside>

        <!-- Main Content -->
        <main class="content-area" id="contentArea">
            <!-- Executive Project Context Card -->
            <section class="project-hero">
                <div class="interview-pillars-bar">
                    <span class="pillar-pill">1. Client Request</span>
                    <span class="pillar-pill">2. Industry Visit</span>
                    <span class="pillar-pill">3. Blueprint</span>
                    <span class="pillar-pill">4. 3-Dev Core Team</span>
                    <span class="pillar-pill">5. 40–50% Backend</span>
                    <span class="pillar-pill">6. Live ROI</span>
                </div>
                <div class="hero-title-group">
                    <h2 class="hero-title">AutoTaskX — Digital Twin &amp; Data Engineer Guide</h2>
                    <span class="badge-live">Active 24/7</span>
                </div>
                <p class="hero-subtitle">
                    বাংলাদেশের একটি শীর্ষস্থানীয় টেক্সটাইল গ্রুপের প্রোজেক্ট — ক্লায়েন্ট আমাদের অফিসে এসে পূর্ণ অটোমেশন ও Digital Twin (ডিজিটাল টুইন) চান; এরপর ইন্ডাস্ট্রি ভিজিট, রিকোয়ারমেন্টস, সফটওয়্যার ব্লুপ্রিন্ট ও ৪ মাসে ২৪/৭ লাইভ প্রোডাকশন।
                </p>

                <div class="meta-grid">
                    <div class="meta-item">
                        <span class="meta-label">Target Role</span>
                        <span class="meta-value">Digital Twin &amp; Data Engineer</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Team &amp; Contribution</span>
                        <span class="meta-value">3-Dev Core Team · Main Backend Engineer (~40–50%)</span>
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

for idx, s in enumerate(slides):
    formatted_speech = format_speech(s['speech'])

    html_content += f"""
            <article class="slide-card{' focus-active' if idx == 0 else ''}" id="slide-{s['num']}" data-index="{idx}" data-label="Slide {s['num']} / {len(slides):02d}" data-search="{html.escape(s['raw_title'])} {html.escape(s['pillar'])} {html.escape(s['objective'])} {html.escape(s['speech'][:240])}">
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
                            View Slide ↗
                        </a>
                    </div>
                </div>

                <div class="objective-box">
                    <div class="objective-label">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="12 8 8 12 12 16 12 8"></polygon></svg>
                        স্লাইডের মূল লক্ষ্য (Slide Objective)
                    </div>
                    {highlight_inline_tokens(html.escape(s['objective']))}
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
                        Technical Quick Reference
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
html_content += f"""
            <!-- Technical Q&A Section -->
            <section class="cheat-sheet-section" id="cheat-sheet" data-index="{len(slides)}" data-label="6 Key Q&amp;As">
                <span class="section-header-badge">Interview Panel Master Cheat Sheet</span>
                <h2 class="section-main-title">6 Key Technical Questions &amp; Fluent English Answers</h2>
                <p class="section-subtext">Easy-to-read international English answers for Digital Twin &amp; Data Engineer interviews (with Bangla pronunciation for tricky words).</p>
"""

for cq in cheat_questions:
    formatted_q = highlight_inline_tokens(html.escape(cq['title']))
    formatted_ans = format_answer(cq['answer'])
    html_content += f"""
                <div class="qa-card">
                    <div class="qa-header">
                        <div class="qa-q">প্রশ্ন {cq['num']}: &ldquo;{formatted_q}&rdquo;</div>
                        <button class="btn-copy" onclick="copySpeech('qa-ans-{cq['num']}', this)">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                            Copy Answer
                        </button>
                    </div>
                    <div class="qa-ans" id="qa-ans-{cq['num']}">
                        <strong>Answer:</strong><br>
                        &ldquo;{formatted_ans}&rdquo;
                    </div>
                </div>
"""

html_content += """
            </section>
        </main>
    </div>

    <!-- Mobile Bottom Sticky Navigation Bar -->
    <nav class="mobile-bottom-nav" aria-label="Mobile Slide Navigation">
        <button class="mnav-btn" id="mobilePrev" type="button">← Prev</button>
        <button class="mnav-jump" id="mobileJump" type="button">Slide 01 / 18 ▾</button>
        <button class="mnav-btn" id="mobileNext" type="button">Next →</button>
    </nav>

    <!-- Mobile Slide Jump Drawer -->
    <div class="drawer-backdrop" id="drawerBackdrop"></div>
    <aside class="mobile-drawer" id="mobileDrawer" aria-hidden="true">
        <div class="mobile-drawer-header">
            <h3>Jump to Slide or Q&amp;A</h3>
            <button class="btn-ctrl" id="closeDrawerBtn" type="button">✕ Close</button>
        </div>
        <div class="mobile-drawer-list" id="mobileDrawerList">
"""

for idx, s in enumerate(slides):
    html_content += f"""            <a href="#slide-{s['num']}" class="mobile-drawer-item{' active' if idx == 0 else ''}" data-index="{idx}">
                <span class="nav-num">{s['num']}</span>
                <div class="mobile-drawer-titles">
                    <span class="mobile-drawer-en">{html.escape(s['en_title'])}</span>
                    {f'<span class="mobile-drawer-bn">{html.escape(s["bn_title"])}</span>' if s['bn_title'] else ''}
                </div>
            </a>\n"""

html_content += f"""            <a href="#cheat-sheet" class="mobile-drawer-item" data-index="{len(slides)}">
                <span class="nav-num">⚡</span>
                <div class="mobile-drawer-titles">
                    <span class="mobile-drawer-en">Master Cheat Sheet (6 Q&amp;As)</span>
                    <span class="mobile-drawer-bn">ইন্টারভিউ প্রশ্নোত্তর পর্ব</span>
                </div>
            </a>
        </div>
    </aside>

    <!-- Toast Component -->
    <div class="toast" id="toastBox">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
        <span id="toastMsg">Copied to clipboard!</span>
    </div>

    <script>
        function fallbackCopyText(text) {{
            const ta = document.createElement('textarea');
            ta.value = text;
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.select();
            try {{ document.execCommand('copy'); }} catch (e) {{}}
            document.body.removeChild(ta);
        }}

        function copySpeech(elementId, btn) {{
            const el = document.getElementById(elementId);
            if (!el) return;
            const text = el.innerText;
            const done = () => {{
                showToast("Copied to clipboard!");
                const originalText = btn.innerHTML;
                btn.innerHTML = '✓ Copied!';
                btn.style.color = '#059669';
                setTimeout(() => {{
                    btn.innerHTML = originalText;
                    btn.style.color = '';
                }}, 1800);
            }};
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(text).then(done).catch(() => {{ fallbackCopyText(text); done(); }});
            }} else {{
                fallbackCopyText(text);
                done();
            }}
        }}

        function showToast(msg) {{
            const toast = document.getElementById('toastBox');
            const toastMsg = document.getElementById('toastMsg');
            toastMsg.innerText = msg;
            toast.classList.add('show');
            setTimeout(() => {{
                toast.classList.remove('show');
            }}, 2200);
        }}

        // Search across slides & Q&A
        const searchInput = document.getElementById('searchInput');
        const searchClear = document.getElementById('searchClear');
        const slideCards = Array.from(document.querySelectorAll('.slide-card'));
        const cheatSection = document.getElementById('cheat-sheet');
        const allSections = [...slideCards, cheatSection].filter(Boolean);

        function applySearch() {{
            const q = searchInput.value.toLowerCase().trim();
            searchClear.classList.toggle('visible', q.length > 0);
            if (q && document.body.classList.contains('focus-mode')) {{
                setFocusMode(false);
            }}
            slideCards.forEach(card => {{
                const searchData = (card.getAttribute('data-search') || '').toLowerCase();
                const textContent = card.innerText.toLowerCase();
                card.style.display = (!q || searchData.includes(q) || textContent.includes(q)) ? '' : 'none';
            }});
            if (cheatSection) {{
                const qaText = cheatSection.innerText.toLowerCase();
                cheatSection.style.display = (!q || qaText.includes(q)) ? '' : 'none';
            }}
        }}

        searchInput.addEventListener('input', applySearch);
        searchClear.addEventListener('click', () => {{
            searchInput.value = '';
            applySearch();
            searchInput.focus();
        }});

        // Scroll progress bar
        window.addEventListener('scroll', () => {{
            const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
            document.getElementById('progressBar').style.width = scrolled + '%';
        }}, {{ passive: true }});

        // Active section tracking & navigation
        let currentIndex = 0;
        const mobilePrev = document.getElementById('mobilePrev');
        const mobileNext = document.getElementById('mobileNext');
        const mobileJump = document.getElementById('mobileJump');

        function updateActiveUI(index) {{
            if (index < 0) index = 0;
            if (index >= allSections.length) index = allSections.length - 1;
            currentIndex = index;

            const activeSection = allSections[index];
            const activeId = activeSection ? activeSection.getAttribute('id') : '';
            const label = activeSection ? activeSection.getAttribute('data-label') : '';

            if (mobileJump && label) {{
                mobileJump.innerText = label + ' ▾';
            }}
            if (mobilePrev) mobilePrev.disabled = (index === 0);
            if (mobileNext) mobileNext.disabled = (index === allSections.length - 1);

            document.querySelectorAll('.sidebar .nav-item').forEach(item => {{
                if (item.getAttribute('href') === '#' + activeId) {{
                    item.classList.add('active');
                    item.scrollIntoView({{ block: 'nearest' }});
                }} else {{
                    item.classList.remove('active');
                }}
            }});

            document.querySelectorAll('.mobile-drawer-item').forEach(item => {{
                const itemIdx = parseInt(item.getAttribute('data-index'), 10);
                item.classList.toggle('active', itemIdx === index);
            }});

            allSections.forEach((sec, idx) => {{
                sec.classList.toggle('focus-active', idx === index);
            }});
        }}

        function goToSection(index) {{
            if (index < 0) index = 0;
            if (index >= allSections.length) index = allSections.length - 1;
            updateActiveUI(index);
            const target = allSections[index];
            if (!target) return;
            if (document.body.classList.contains('focus-mode')) {{
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }} else {{
                target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}

        const observer = new IntersectionObserver((entries) => {{
            if (document.body.classList.contains('focus-mode')) return;
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    const idx = parseInt(entry.target.getAttribute('data-index'), 10);
                    if (!isNaN(idx)) updateActiveUI(idx);
                }}
            }});
        }}, {{ threshold: 0.25, rootMargin: '-80px 0px -40% 0px' }});

        allSections.forEach(section => observer.observe(section));

        if (mobilePrev) mobilePrev.addEventListener('click', () => goToSection(currentIndex - 1));
        if (mobileNext) mobileNext.addEventListener('click', () => goToSection(currentIndex + 1));

        // Mobile Slide Drawer
        const mobileDrawer = document.getElementById('mobileDrawer');
        const drawerBackdrop = document.getElementById('drawerBackdrop');
        const openDrawerBtn = document.getElementById('openDrawerBtn');
        const closeDrawerBtn = document.getElementById('closeDrawerBtn');

        function openDrawer() {{
            mobileDrawer.classList.add('open');
            drawerBackdrop.classList.add('open');
            mobileDrawer.setAttribute('aria-hidden', 'false');
            document.body.classList.add('drawer-open');
        }}

        function closeDrawer() {{
            mobileDrawer.classList.remove('open');
            drawerBackdrop.classList.remove('open');
            mobileDrawer.setAttribute('aria-hidden', 'true');
            document.body.classList.remove('drawer-open');
        }}

        if (openDrawerBtn) openDrawerBtn.addEventListener('click', openDrawer);
        if (mobileJump) mobileJump.addEventListener('click', openDrawer);
        if (closeDrawerBtn) closeDrawerBtn.addEventListener('click', closeDrawer);
        if (drawerBackdrop) drawerBackdrop.addEventListener('click', closeDrawer);

        document.querySelectorAll('.mobile-drawer-item').forEach(item => {{
            item.addEventListener('click', (e) => {{
                e.preventDefault();
                const idx = parseInt(item.getAttribute('data-index'), 10);
                closeDrawer();
                setTimeout(() => goToSection(idx), 60);
            }});
        }});

        // Single-Slide Focus Mode (with touch swipe!)
        const focusBtn = document.getElementById('focusToggle');
        function setFocusMode(enabled) {{
            document.body.classList.toggle('focus-mode', enabled);
            if (focusBtn) {{
                focusBtn.classList.toggle('active-state', enabled);
                focusBtn.innerHTML = enabled ? '📜 All' : '🎯 Focus';
            }}
            try {{ localStorage.setItem('ax_guide_focus', enabled ? '1' : '0'); }} catch (e) {{}}
            if (enabled) {{
                searchInput.value = '';
                applySearch();
                updateActiveUI(currentIndex);
                window.scrollTo({{ top: 0, behavior: 'smooth' }});
            }}
        }}

        if (focusBtn) {{
            focusBtn.addEventListener('click', () => {{
                setFocusMode(!document.body.classList.contains('focus-mode'));
            }});
        }}

        // Touch swipe in Focus Mode
        let touchStartX = 0;
        let touchStartY = 0;
        const contentArea = document.getElementById('contentArea');
        if (contentArea) {{
            contentArea.addEventListener('touchstart', (e) => {{
                if (e.changedTouches && e.changedTouches.length === 1) {{
                    touchStartX = e.changedTouches[0].clientX;
                    touchStartY = e.changedTouches[0].clientY;
                }}
            }}, {{ passive: true }});
            contentArea.addEventListener('touchend', (e) => {{
                if (!document.body.classList.contains('focus-mode')) return;
                if (!e.changedTouches || e.changedTouches.length !== 1) return;
                const dx = e.changedTouches[0].clientX - touchStartX;
                const dy = e.changedTouches[0].clientY - touchStartY;
                if (Math.abs(dx) > 65 && Math.abs(dx) > Math.abs(dy) * 1.4) {{
                    if (dx < 0) goToSection(currentIndex + 1);
                    else goToSection(currentIndex - 1);
                }}
            }}, {{ passive: true }});
        }}

        // Pronunciation Toggle
        const pronBtn = document.getElementById('pronToggle');
        function setPronVisible(visible) {{
            document.body.classList.toggle('hide-pron', !visible);
            if (pronBtn) pronBtn.classList.toggle('active-state', visible);
            try {{ localStorage.setItem('ax_guide_pron', visible ? 'on' : 'off'); }} catch (e) {{}}
        }}
        if (localStorage.getItem('ax_guide_pron') === 'off') setPronVisible(false);
        if (pronBtn) {{
            pronBtn.addEventListener('click', () => {{
                setPronVisible(document.body.classList.contains('hide-pron'));
            }});
        }}

        // Dark/Light Theme Toggle (persisted)
        const themeBtn = document.getElementById('themeToggle');
        const currentTheme = localStorage.getItem('ax_guide_theme') || 'light';
        if (currentTheme === 'dark') {{
            document.documentElement.setAttribute('data-theme', 'dark');
            themeBtn.innerText = '☀️';
        }}

        themeBtn.addEventListener('click', () => {{
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {{
                document.documentElement.removeAttribute('data-theme');
                themeBtn.innerText = '🌙';
                localStorage.setItem('ax_guide_theme', 'light');
            }} else {{
                document.documentElement.setAttribute('data-theme', 'dark');
                themeBtn.innerText = '☀️';
                localStorage.setItem('ax_guide_theme', 'dark');
            }}
        }});

        // Font Size Controls (persisted, comfy range 14px - 24px)
        const defaultFont = window.innerWidth <= 768 ? 17 : 16;
        let currentFontSize = parseInt(localStorage.getItem('ax_guide_fontsize') || '', 10) || defaultFont;
        document.documentElement.style.setProperty('--base-font-size', currentFontSize + 'px');

        document.getElementById('fontInc').addEventListener('click', () => {{
            if (currentFontSize < 24) {{
                currentFontSize += 1;
                document.documentElement.style.setProperty('--base-font-size', currentFontSize + 'px');
                try {{ localStorage.setItem('ax_guide_fontsize', String(currentFontSize)); }} catch (e) {{}}
                showToast('Font: ' + currentFontSize + 'px');
            }}
        }});

        document.getElementById('fontDec').addEventListener('click', () => {{
            if (currentFontSize > 13) {{
                currentFontSize -= 1;
                document.documentElement.style.setProperty('--base-font-size', currentFontSize + 'px');
                try {{ localStorage.setItem('ax_guide_fontsize', String(currentFontSize)); }} catch (e) {{}}
                showToast('Font: ' + currentFontSize + 'px');
            }}
        }});

        // Keyboard navigation (desktop)
        window.addEventListener('keydown', (e) => {{
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            if (e.key === 'j' || e.key === 'ArrowDown' || (document.body.classList.contains('focus-mode') && e.key === 'ArrowRight')) {{
                e.preventDefault();
                goToSection(currentIndex + 1);
            }} else if (e.key === 'k' || e.key === 'ArrowUp' || (document.body.classList.contains('focus-mode') && e.key === 'ArrowLeft')) {{
                e.preventDefault();
                goToSection(currentIndex - 1);
            }} else if (e.key === 'Escape') {{
                closeDrawer();
            }}
        }});

        updateActiveUI(0);
    </script>
</body>
</html>
"""

with open('guide.html', 'w', encoding='utf-8') as out_f:
    out_f.write(html_content)

print(f"Generated guide.html successfully. Size: {len(html_content)} bytes.")
