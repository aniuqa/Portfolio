import os

graveyard_labels = {
    "graveyard_0": "Profile Picture Draft v1",
    "graveyard_1": "Profile Picture Draft v2",
    "graveyard_2": "YouTube Banner Draft",
    "graveyard_3": "Thumbnail Iteration A",
    "graveyard_4": "Procreate Pocket Sketch",
    "graveyard_5": "Procreate Pocket Concept",
    "graveyard_6": "Procreate Pocket Artwork",
    "graveyard_7": "Procreate Pocket Study",
    "graveyard_8": "Procreate Pocket Study 2",
    "graveyard_9": "Profile Picture Final Draft"
}

images = []
i = 0
while os.path.exists(f"thumbnail_{i}.jpg"):
    images.append(f"thumbnail_{i}.jpg")
    i += 1

secondary_images = []
j = 0
while os.path.exists(f"2thumbnail_{j}.jpg"):
    secondary_images.append(f"2thumbnail_{j}.jpg")
    j += 1

graveyard_images = []
k = 0
while True:
    found = False
    for ext in ['.jpg', '.JPG', '.png', '.PNG']:
        filename = f"graveyard_{k}{ext}"
        if os.path.exists(filename):
            graveyard_images.append(filename)
            found = True
            break
    if not found and k > 15:
        break
    k += 1
    if k > 20:
        break

if not graveyard_images:
    for old_id in [1, 2, 3, 4, 6]:
        filename = f"old{old_id}.jpg"
        if os.path.exists(filename):
            graveyard_images.append(filename)

gallery_html = ""
for idx, img in enumerate(images, start=1):
    gallery_html += f'''
                <div class="grid-item" onclick="zoomThumbnail(this, '{img}')">
                    <img src="{img}" alt="Thumbnail {idx}" loading="lazy" decoding="async">
                    <div class="date-overlay">Thumbnail {idx}</div>
                </div>'''

secondary_gallery_html = ""
for idx, img in enumerate(secondary_images, start=1):
    secondary_gallery_html += f'''
                <div class="grid-item" onclick="zoomThumbnail(this, '{img}')">
                    <img src="{img}" alt="Thumbnail {idx}" loading="lazy" decoding="async">
                    <div class="date-overlay">Thumbnail {idx}</div>
                </div>'''

graveyard_html = ""
for g_img in graveyard_images:
    base_name = os.path.splitext(g_img)[0]
    label = graveyard_labels.get(base_name, "Archive Draft")
    graveyard_html += f'''
                <div class="grid-item" onclick="zoomThumbnail(this, '{g_img}')">
                    <img src="{g_img}" alt="Graveyard Iteration" loading="lazy" decoding="async">
                    <div class="date-overlay">{label}</div>
                </div>'''

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GHUYD LAPAZ — Professional Portfolio</title>
    <style>
        :root {
            --bg-color: #121011;
            --surface-glass: #1b1719;
            --surface-glass-hover: #231e21;
            --border-glass: rgba(255, 235, 225, 0.08);
            --border-glass-hover: rgba(246, 173, 141, 0.4);
            --accent-color: #f6ad8d;
            --accent-glow: rgba(246, 173, 141, 0.15);
            --text-primary: #fdf8f6;
            --text-secondary: #b8a9a4;
            --smooth-easing: cubic-bezier(0.25, 1, 0.5, 1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-color);
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(255, 183, 178, 0.13) 0%, transparent 45%),
                radial-gradient(circle at 85% 85%, rgba(255, 218, 185, 0.11) 0%, transparent 45%),
                radial-gradient(circle at 50% 50%, rgba(246, 173, 141, 0.06) 0%, transparent 60%);
            background-size: 200% 200%;
            background-attachment: fixed;
            animation: ambientShift 24s ease infinite alternate;
            color: var(--text-primary);
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            padding: 60px 20px;
            overflow-x: hidden;
        }

        @keyframes ambientShift {
            0% { background-position: 0% 0%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 50% 100%; }
        }

        .wrapper {
            width: 100%;
            max-width: 1350px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        header {
            margin-bottom: 70px;
            padding-bottom: 50px;
            border-bottom: 1px solid var(--border-glass);
            display: grid;
            grid-template-columns: 1.35fr 1fr;
            gap: 30px;
            align-items: stretch;
        }

        .header-content {
            background-color: var(--surface-glass);
            border: 1px solid var(--border-glass);
            border-radius: 28px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: border-color 0.2s ease, background-color 0.2s ease;
        }

        .header-content.expandable-card {
            cursor: pointer;
            user-select: none;
        }

        .header-content.expandable-card:hover {
            border-color: var(--border-glass-hover);
            background-color: var(--surface-glass-hover);
        }

        .header-top-row {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 20px;
        }

        .header-sidebar {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .info-card {
            background-color: var(--surface-glass);
            border: 1px solid var(--border-glass);
            border-radius: 22px;
            padding: 24px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, background-color 0.15s ease, border-color 0.15s ease;
            will-change: transform;
        }

        .info-card:hover {
            transform: translateY(-2px);
            background-color: var(--surface-glass-hover);
            border-color: var(--border-glass-hover);
        }

        .card-logo {
            width: 18px;
            height: 18px;
            object-fit: contain;
            display: inline-block;
            vertical-align: middle;
            flex-shrink: 0;
            filter: brightness(0) invert(1);
        }

        .card-logo.original-color {
            filter: none;
        }

        .info-card h3 {
            font-size: 0.95rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
            letter-spacing: -0.01em;
        }

        .interactive-card {
            background: linear-gradient(135deg, rgba(246, 173, 141, 0.08) 0%, #1b1719 100%);
            border: 1px solid rgba(246, 173, 141, 0.25);
            text-decoration: none;
            cursor: pointer;
        }

        .interactive-card:hover {
            background: linear-gradient(135deg, rgba(246, 173, 141, 0.15) 0%, #231e21 100%);
            border-color: var(--accent-color);
            box-shadow: 0 10px 25px var(--accent-glow);
        }

        .widget-top-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 14px;
        }

        .widget-left-group {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .widget-pfp {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid var(--accent-color);
            background-color: #231e21;
            flex-shrink: 0;
        }

        .widget-pfp img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .widget-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.01em;
        }

        .widget-subtitle {
            font-size: 0.8rem;
            color: var(--text-secondary);
        }

        .external-icon {
            font-size: 1.1rem;
            color: var(--accent-color);
            font-weight: bold;
            transition: transform 0.15s ease;
        }

        .interactive-card:hover .external-icon {
            transform: translate(2px, -2px);
        }

        .info-card p {
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 2px;
            line-height: 1.4;
        }

        /* Universal Expandable Cards */
        .expandable-card {
            cursor: pointer;
            user-select: none;
        }

        .expandable-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
        }

        .expand-arrow {
            font-size: 0.85rem;
            color: var(--accent-color);
            transition: transform 0.3s ease;
            font-weight: bold;
            flex-shrink: 0;
        }

        .expandable-card.open .expand-arrow {
            transform: rotate(90deg);
        }

        .expandable-content {
            max-height: 0;
            overflow: hidden;
            opacity: 0;
            transition: max-height 0.5s ease, opacity 0.4s ease, margin-top 0.4s ease, padding 0.4s ease;
            margin-top: 0;
            padding-top: 0;
            padding-bottom: 0;
        }

        .expandable-card.open .expandable-content {
            max-height: 1200px;
            opacity: 1;
            margin-top: 20px;
            border-top: 1px solid var(--border-glass);
            padding-top: 20px;
        }

        .tools-section-title {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #ffffff;
            font-weight: 600;
            margin-bottom: 8px;
            margin-top: 8px;
        }

        .tools-pills-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 10px;
        }

        .tool-pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            padding: 5px 10px;
            border-radius: 12px;
            font-size: 0.78rem;
            color: #fdf8f6;
            font-weight: 500;
        }

        .tool-pill img {
            width: 14px;
            height: 14px;
            object-fit: contain;
            border-radius: 3px;
        }

        h1 {
            font-size: 2.8rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            color: #ffffff;
            margin-bottom: 8px;
        }

        .ios-widget-badge {
            font-size: 0.72rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent-color);
            background: rgba(246, 173, 141, 0.1);
            padding: 5px 12px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 12px;
            border: 1px solid rgba(246, 173, 141, 0.2);
        }

        .contacts-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-top: 0;
        }

        .contact-drawer-card {
            background-color: #211c1f;
            border: 1px solid var(--border-glass);
            border-radius: 16px;
            overflow: hidden;
            transition: border-color 0.15s ease, background-color 0.15s ease;
            cursor: pointer;
        }

        .contact-drawer-card:hover {
            border-color: rgba(246, 173, 141, 0.4);
            background-color: #292326;
        }

        .contact-drawer-header {
            padding: 14px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            user-select: none;
        }

        .contact-drawer-title {
            font-size: 0.9rem;
            font-weight: 600;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .contact-drawer-content {
            max-height: 0;
            overflow: hidden;
            opacity: 0;
            transition: max-height 0.35s ease, opacity 0.25s ease, padding 0.35s ease;
            background: #171315;
            padding: 0 18px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .contact-drawer-card.open .contact-drawer-content {
            max-height: 60px;
            opacity: 1;
            padding: 14px 18px;
            border-top: 1px solid var(--border-glass);
        }

        .contact-drawer-content a, .contact-drawer-content code {
            font-size: 0.9rem;
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 600;
        }

        .contact-drawer-content a:hover {
            text-decoration: underline;
        }

        .subtitle {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: 0;
            font-weight: 400;
        }

        .bio-text {
            font-size: 0.98rem;
            color: #c5b8b3;
            line-height: 1.75;
            text-align: justify;
        }

        section {
            margin-bottom: 60px;
        }

        .section-divider {
            margin: 80px 0;
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--border-glass), transparent);
        }

        h2 {
            font-size: 1.25rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 20px;
            letter-spacing: -0.01em;
        }

        .channel-header-row {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 16px;
        }

        .channel-pfp {
            width: 52px;
            height: 52px;
            border-radius: 50%;
            overflow: hidden;
            border: 2px solid var(--accent-color);
            flex-shrink: 0;
            background-color: #231e21;
        }

        .channel-pfp img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .channel-title-link {
            font-size: 1.4rem;
            font-weight: 700;
            color: #ffffff;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            letter-spacing: -0.01em;
            transition: color 0.15s ease;
        }

        .channel-title-link:hover {
            color: var(--accent-color);
            text-decoration: underline;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.2rem;
            margin-bottom: 24px;
        }

        .stat-card {
            background-color: var(--surface-glass);
            border: 1px solid var(--border-glass);
            border-radius: 20px;
            padding: 22px;
            text-align: left;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s ease, border-color 0.15s ease, background-color 0.15s ease;
            will-change: transform;
        }

        .stat-card:hover {
            transform: translateY(-2px);
            border-color: var(--border-glass-hover);
            background-color: var(--surface-glass-hover);
        }

        .stat-number {
            font-size: 1.7rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 4px;
            letter-spacing: -0.02em;
        }

        .stat-label {
            font-size: 0.72rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.2rem;
            width: 100%;
        }

        .grid-item {
            position: relative;
            background-color: var(--surface-glass);
            border: 1px solid var(--border-glass);
            border-radius: 18px;
            overflow: hidden;
            aspect-ratio: 16 / 9;
            cursor: pointer;
            transition: transform 0.2s ease, border-color 0.15s ease, box-shadow 0.15s ease;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
            will-change: transform;
        }

        .grid-item:hover {
            border-color: var(--accent-color);
            transform: translateY(-3px);
            box-shadow: 0 10px 25px var(--accent-glow);
            z-index: 10;
        }

        .grid-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.25s ease;
        }

        .grid-item:hover img {
            transform: scale(1.03);
        }

        .date-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 20px 14px 12px 14px;
            background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 100%);
            color: #ffffff;
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            opacity: 0;
            transform: translateY(6px);
            transition: opacity 0.15s ease, transform 0.15s ease;
            text-align: left;
        }

        .grid-item:hover .date-overlay {
            opacity: 1;
            transform: translateY(0);
        }

        .coffee-container {
            display: flex;
            justify-content: center;
            margin: 80px 0 20px 0;
        }

        .coffee-btn {
            background-color: var(--accent-color);
            color: #121011;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 15px 32px;
            border-radius: 30px;
            text-decoration: none;
            box-shadow: 0 8px 25px var(--accent-glow);
            transition: transform 0.2s ease, background-color 0.15s ease;
            will-change: transform;
        }

        .coffee-btn:hover {
            transform: translateY(-2px);
            background-color: #ffc4a8;
            box-shadow: 0 12px 30px rgba(246, 173, 141, 0.4);
        }

        #iosZoomOverlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(18, 16, 17, 0.88);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            z-index: 9999;
            display: none;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.25s ease;
            pointer-events: none;
        }

        #iosZoomOverlay.active {
            opacity: 1;
            pointer-events: auto;
        }

        #iosZoomImg {
            position: absolute;
            object-fit: contain;
            border-radius: 22px;
            will-change: transform, width, height;
            transform-origin: top left;
            transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), border-radius 0.35s ease, box-shadow 0.35s ease;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 30px rgba(246, 173, 141, 0.12);
        }

        footer {
            border-top: 1px solid var(--border-glass);
            padding-top: 35px;
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        footer a {
            color: #ffffff;
            text-decoration: none;
            font-weight: 500;
        }

        @media (max-width: 1100px) {
            header {
                grid-template-columns: 1fr;
            }
            .stats-grid, .grid-container, .contacts-grid {
                grid-template-columns: repeat(1, 1fr);
            }
        }
    </style>
</head>
<body>

    <div class="wrapper">
        <header>
            <!-- Expandable Main Bio Header Card -->
            <div class="header-content expandable-card" id="card-main-bio" onclick="toggleIndependentExpandable('card-main-bio')">
                <div class="header-top-row">
                    <div>
                        <span class="ios-widget-badge">Personal & Career Details</span>
                        <h1>GHUYD LAPAZ</h1>
                        <p class="subtitle">I learned to make people click before I ever called myself a designer.</p>
                    </div>
                    <div class="expand-arrow" style="margin-top: 12px;">▶</div>
                </div>

                <div class="expandable-content" onclick="event.stopPropagation()">
                    <p class="bio-text" style="margin-bottom: 30px;">I started creating content on YouTube at exactly 14 years old. My foundational design instincts were built entirely on mobile constraints without a single AI shortcut, purely because AI wasn't that prevalent back then (2018–2022). Armed with an Oppo A7, zero budget, and sheer resourcefulness, I edited every video and designed every thumbnail from scratch on mobile using Pixelmator. By 2020, through channel revenue earned from scaling my content to over 4.25M+ views and 60K+ subscribers, I bought an iPhone 11 and proudly purchased Pixelmator legally—which eventually caught the software company's eye, leading to a direct partnership offer. Coupled with early hands-on lab experience with desktop Photoshop during my Senior High School animation ICT coursework, I know how to execute under any condition. By late 2025, I finally secured my current desktop rig, ready to scale up output and speed.</p>
                    
                    <div class="contacts-grid">
                        <div class="contact-drawer-card expandable-card" id="drawer-phone" onclick="toggleIndependentExpandable('drawer-phone')">
                            <div class="contact-drawer-header">
                                <div class="contact-drawer-title"><img src="telephone.png" alt="Phone" class="card-logo"> Phone</div>
                                <div class="expand-arrow">▶</div>
                            </div>
                            <div class="contact-drawer-content" onclick="event.stopPropagation()">
                                <a href="tel:+639997387979">+639997387979</a>
                            </div>
                        </div>

                        <div class="contact-drawer-card expandable-card" id="drawer-discord" onclick="toggleIndependentExpandable('drawer-discord')">
                            <div class="contact-drawer-header">
                                <div class="contact-drawer-title"><img src="discord.png" alt="Discord" class="card-logo"> Discord</div>
                                <div class="expand-arrow">▶</div>
                            </div>
                            <div class="contact-drawer-content" onclick="event.stopPropagation()">
                                <code>gyd.000000</code>
                            </div>
                        </div>

                        <div class="contact-drawer-card expandable-card" id="drawer-email" onclick="toggleIndependentExpandable('drawer-email')">
                            <div class="contact-drawer-header">
                                <div class="contact-drawer-title"><img src="email.png" alt="Email" class="card-logo"> Email</div>
                                <div class="expand-arrow">▶</div>
                            </div>
                            <div class="contact-drawer-content" onclick="event.stopPropagation()">
                                <a href="mailto:might370@gmail.com">might370@gmail.com</a>
                            </div>
                        </div>

                        <div class="contact-drawer-card expandable-card" id="drawer-linkedin" onclick="toggleIndependentExpandable('drawer-linkedin')">
                            <div class="contact-drawer-header">
                                <div class="contact-drawer-title"><img src="linkedin.png" alt="LinkedIn" class="card-logo original-color"> LinkedIn</div>
                                <div class="expand-arrow">▶</div>
                            </div>
                            <div class="contact-drawer-content" onclick="event.stopPropagation()">
                                <a href="https://linkedin.com" target="_blank">linkedin.com/in/ghuyd-lapaz</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="header-sidebar">
                <a href="#asceor-section" class="info-card interactive-card" onclick="smoothScrollTo(event, 'asceor-section')">
                    <div class="widget-top-row">
                        <div class="widget-left-group">
                            <div class="widget-pfp">
                                <img src="pfp_2.jpg" alt="Asceor PFP" loading="lazy" decoding="async" onerror="this.style.display='none'">
                            </div>
                            <div>
                                <div class="widget-title">asceor</div>
                                <div class="widget-subtitle">Secondary experimental channel</div>
                            </div>
                        </div>
                        <div class="external-icon">↗</div>
                    </div>
                </a>

                <!-- Origin Era Expandable Card -->
                <div class="info-card expandable-card" id="card-origin" onclick="toggleIndependentExpandable('card-origin')">
                    <div class="expandable-header">
                        <h3><img src="iphone.png" alt="iPhone" class="card-logo"> Origin Era (Mobile)</h3>
                        <div class="expand-arrow">▶</div>
                    </div>
                    <p style="margin-top: 6px;"><strong>Device:</strong> iPhone 11 / Oppo A7</p>
                    <div class="expandable-content">
                        <div class="tools-section-title">For Image Editing</div>
                        <div class="tools-pills-grid">
                            <div class="tool-pill"><img src="pixelmator.jpg" alt="Pixelmator" onerror="this.style.display='none'"> Pixelmator</div>
                            <div class="tool-pill"><img src="photoshop.png" alt="Photoshop" onerror="this.style.display='none'"> PS Photoshop Mobile</div>
                        </div>
                        <div class="tools-section-title">For Video Editing</div>
                        <div class="tools-pills-grid">
                            <div class="tool-pill"><img src="capcut.png" alt="CapCut" onerror="this.style.display='none'"> CapCut Mobile</div>
                            <div class="tool-pill"><img src="vllo.png" alt="VLLO" onerror="this.style.display='none'"> VLLO</div>
                            <div class="tool-pill"><img src="kinemaster.jpeg" alt="KineMaster" onerror="this.style.display='none'"> KineMaster</div>
                            <div class="tool-pill"><img src="imovie.png" alt="iMovie" onerror="this.style.display='none'"> iMovie</div>
                        </div>
                        <p style="font-size: 0.78rem; color: var(--text-secondary); margin-top: 4px;">Hands-on practical experience executing mobile-first creative workflows.</p>
                    </div>
                </div>

                <!-- Desktop Rig Expandable Card -->
                <div class="info-card expandable-card" id="card-desktop" onclick="toggleIndependentExpandable('card-desktop')">
                    <div class="expandable-header">
                        <h3><img src="computer.png" alt="Computer" class="card-logo"> Current Desktop Rig</h3>
                        <div class="expand-arrow">▶</div>
                    </div>
                    <p style="margin-top: 6px;"><strong>Specs:</strong> Ryzen 5 5600G | GTX 1060 | 16GB RAM</p>
                    <div class="expandable-content">
                        <div class="tools-section-title">For Image Editing</div>
                        <div class="tools-pills-grid">
                            <div class="tool-pill"><img src="photoshop.png" alt="Photoshop" onerror="this.style.display='none'"> Photoshop</div>
                            <div class="tool-pill"><img src="lightroom.png" alt="Lightroom" onerror="this.style.display='none'"> Lightroom Classic</div>
                        </div>
                        <div class="tools-section-title">For Video Editing</div>
                        <div class="tools-pills-grid">
                            <div class="tool-pill"><img src="capcut.png" alt="CapCut" onerror="this.style.display='none'"> CapCut Desktop</div>
                            <div class="tool-pill"><img src="clipchamp.png" alt="Clipchamp" onerror="this.style.display='none'"> Microsoft Clipchamp</div>
                        </div>
                        <p style="font-size: 0.78rem; color: var(--text-secondary); margin-top: 4px;">Advanced desktop setup for high-speed production and design scaling.</p>
                    </div>
                </div>
            </div>
        </header>

        <section>
            <div class="channel-header-row">
                <div class="channel-pfp">
                    <img src="pfp_1.jpg" alt="Unarmed PFP" loading="lazy" decoding="async" onerror="this.style.display='none'">
                </div>
                <div>
                    <a href="https://www.youtube.com/@Unarmed143" target="_blank" class="channel-title-link">Primary Channel: Unarmed ↗</a>
                </div>
            </div>
            <p style="color: var(--text-secondary); margin-bottom: 20px;">The foundation of my content creation journey. Built from scratch on mobile, this channel drove over 4.25M+ total views and 61K+ subscribers through high-retention gaming content and psychological thumbnail packaging. It's all about Mobile Legends where I primarily create gameplays, in-depth tutorials, tips and tricks, guides, and some montage.</p>
            
            <div>
                <h2>Channel Telemetry</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-number">4.25M+</div>
                        <div class="stat-label">Total Views</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">61.4K</div>
                        <div class="stat-label">Subscribers</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">63.0K</div>
                        <div class="stat-label">Peak Subs</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">1.47M</div>
                        <div class="stat-label">Top Video Views</div>
                    </div>
                </div>
            </div>

            <div style="margin-top: 25px;">
                <div class="grid-container">
                    __GALLERY_HTML__
                </div>
            </div>
        </section>

        <hr class="section-divider">

        <section id="asceor-section">
            <div class="channel-header-row">
                <div class="channel-pfp">
                    <img src="pfp_2.jpg" alt="Asceor PFP" loading="lazy" decoding="async" onerror="this.style.display='none'">
                </div>
                <div>
                    <a href="https://www.youtube.com/@asceor7611" target="_blank" class="channel-title-link">Secondary Channel: Asceor ↗</a>
                </div>
            </div>
            <p style="color: var(--text-secondary); margin-bottom: 20px;">An experimental mobile FPS hub focusing on Combat Master 2021 and fast-paced tactical content. This secondary channel centers on gameplay testing, optimization guides, lag-fix tutorials, and rapid trend-capitalization.</p>
            
            <div>
                <h2>Secondary Telemetry</h2>
                <div class="stats-grid" style="grid-template-columns: repeat(3, 1fr);">
                    <div class="stat-card">
                        <div class="stat-number">42,809</div>
                        <div class="stat-label">Total Views</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">106</div>
                        <div class="stat-label">Subscribers / Peak</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">41,304</div>
                        <div class="stat-label">Top Video Views</div>
                    </div>
                </div>
            </div>

            <div style="margin-top: 25px;">
                <div class="grid-container">
                    __SECONDARY_GALLERY_HTML__
                </div>
            </div>
        </section>

        <hr class="section-divider">

        <section>
            <h2>Creative Archive & Graveyard</h2>
            <p style="color: var(--text-secondary); margin-bottom: 20px;">Early drafts, experimental assets, and unreleased iterations from past projects.</p>
            <div class="grid-container">
                __GRAVEYARD_HTML__
            </div>
        </section>

        <div class="coffee-container">
            <a href="https://buymeacoffee.com" target="_blank" class="coffee-btn">Buy me a coffee ☕</a>
        </div>

        <footer>
            <p>PROFESSIONAL PORTFOLIO // Ghuyd Lapaz &nbsp;|&nbsp; Contact: <a href="mailto:might370@gmail.com">might370@gmail.com</a></p>
        </footer>
    </div>

    <div id="iosZoomOverlay" onclick="closeIosZoom()">
        <img id="iosZoomImg" src="" alt="Zoomed View">
    </div>

    <script>
        function smoothScrollTo(event, targetId) {
            event.preventDefault();
            const target = document.getElementById(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        function toggleIndependentExpandable(cardId) {
            const card = document.getElementById(cardId);
            if (card) {
                card.classList.toggle('open');
            }
        }

        let activeZoomElement = null;

        function zoomThumbnail(element, imgSrc) {
            activeZoomElement = element;
            const thumbImg = element.querySelector('img');
            const rect = thumbImg.getBoundingClientRect();
            
            const overlay = document.getElementById('iosZoomOverlay');
            const zoomImg = document.getElementById('iosZoomImg');
            
            zoomImg.src = imgSrc;
            
            const naturalW = thumbImg.naturalWidth || 16;
            const naturalH = thumbImg.naturalHeight || 9;
            const aspectRatio = naturalW / naturalH;
            
            const maxW = window.innerWidth * 0.88;
            const maxH = window.innerHeight * 0.88;
            
            let targetW = maxW;
            let targetH = targetW / aspectRatio;
            
            if (targetH > maxH) {
                targetH = maxH;
                targetW = targetH * aspectRatio;
            }
            
            const targetX = (window.innerWidth - targetW) / 2;
            const targetY = (window.innerHeight - targetH) / 2;
            
            const scaleX = rect.width / targetW;
            const scaleY = rect.height / targetH;
            const translateX = rect.left - targetX;
            const translateY = rect.top - targetY;
            
            zoomImg.style.width = targetW + 'px';
            zoomImg.style.height = targetH + 'px';
            zoomImg.style.borderRadius = '18px';
            zoomImg.style.transition = 'none';
            zoomImg.style.transform = `translate3d(${translateX}px, ${translateY}px, 0) scale(${scaleX}, ${scaleY})`;
            
            overlay.style.display = 'flex';
            void overlay.offsetWidth;
            
            overlay.classList.add('active');
            zoomImg.style.transition = 'transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), border-radius 0.35s ease, box-shadow 0.35s ease';
            zoomImg.style.transform = 'translate3d(0, 0, 0) scale(1, 1)';
            zoomImg.style.borderRadius = '22px';
        }

        function closeIosZoom() {
            const overlay = document.getElementById('iosZoomOverlay');
            const zoomImg = document.getElementById('iosZoomImg');
            
            if (!activeZoomElement) {
                overlay.style.display = 'none';
                overlay.classList.remove('active');
                return;
            }
            
            const thumbImg = activeZoomElement.querySelector('img');
            const rect = thumbImg.getBoundingClientRect();
            
            const naturalW = thumbImg.naturalWidth || 16;
            const naturalH = thumbImg.naturalHeight || 9;
            const aspectRatio = naturalW / naturalH;
            
            const maxW = window.innerWidth * 0.88;
            const maxH = window.innerHeight * 0.88;
            
            let targetW = maxW;
            let targetH = targetW / aspectRatio;
            
            if (targetH > maxH) {
                targetH = maxH;
                targetW = targetH * aspectRatio;
            }
            
            const targetX = (window.innerWidth - targetW) / 2;
            const targetY = (window.innerHeight - targetH) / 2;
            
            const scaleX = rect.width / targetW;
            const scaleY = rect.height / targetH;
            const translateX = rect.left - targetX;
            const translateY = rect.top - targetY;
            
            zoomImg.style.transform = `translate3d(${translateX}px, ${translateY}px, 0) scale(${scaleX}, ${scaleY})`;
            zoomImg.style.borderRadius = '18px';
            overlay.classList.remove('active');
            
            setTimeout(() => {
                overlay.style.display = 'none';
            }, 350);
        }
    </script>
</body>
</html>
"""

final_html = html_template.replace("__GALLERY_HTML__", gallery_html)
final_html = final_html.replace("__SECONDARY_GALLERY_HTML__", secondary_gallery_html)
final_html = final_html.replace("__GRAVEYARD_HTML__", graveyard_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Main intro box successfully turned into an interactive expandable drawer with warm pastel aesthetic!")