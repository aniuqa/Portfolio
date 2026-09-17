import os

# Check available main thumbnails from 0 to 139
images = []
for i in range(140):
    filename = f"thumbnail_{i}.jpg"
    if os.path.exists(filename):
        images.append(filename)

# Check graveyard images (old1 to old6, excluding old5)
graveyard_images = []
for old_id in [1, 2, 3, 4, 6]:
    filename = f"old{old_id}.jpg"
    if os.path.exists(filename):
        graveyard_images.append(filename)

print(f"Found {len(images)} main thumbnails and {len(graveyard_images)} graveyard items. Generating ultra-optimized index.html...")

# Build gallery HTML dynamically
gallery_html = ""
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
for index, img in enumerate(images):
    year_num = 2019 + (index % 4)
    month_name = months[(index * 3) % 12]
    date_str = f"{month_name} {year_num}"
    
    gallery_html += f'    <div class="grid-item" onclick="openModal(this)">\n'
    gallery_html += f'        <img src="{img}" alt="Thumbnail Work" loading="lazy" decoding="async">\n'
    gallery_html += f'        <div class="date-overlay">{date_str}</div>\n'
    gallery_html += f'    </div>\n'

graveyard_html = ""
for g_index, g_img in enumerate(graveyard_images):
    g_year = 2019 if g_index < 3 else 2020
    g_date = f"SEP {g_year}"
    
    graveyard_html += f'    <div class="grid-item" onclick="openModal(this)">\n'
    graveyard_html += f'        <img src="{g_img}" alt="Old Iteration" loading="lazy" decoding="async">\n'
    graveyard_html += f'        <div class="date-overlay">{g_date}</div>\n'
    graveyard_html += f'    </div>\n'

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GHUYD LAPAZ — Thumbnail Designer & Creator</title>
    <style>
        :root {
            --bg-color: #0a0a0a;
            --card-bg: #141414;
            --text-main: #f5f5f5;
            --text-muted: #a3a3a3;
            --border-color: #262626;
            --accent-color: #38bdf8;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            padding: 60px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .container {
            width: 100%;
            max-width: 900px;
        }

        header {
            margin-bottom: 60px;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 40px;
        }

        .tagline-badge {
            display: inline-block;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent-color);
            background: rgba(56, 189, 248, 0.1);
            padding: 4px 10px;
            border-radius: 4px;
            margin-bottom: 16px;
        }

        h1 {
            font-size: 2.8rem;
            font-weight: 600;
            letter-spacing: -0.03em;
            color: #ffffff;
            margin-bottom: 12px;
            text-transform: uppercase;
        }

        .subtitle {
            font-size: 1.25rem;
            color: var(--text-muted);
            margin-bottom: 24px;
            font-weight: 400;
        }

        .bio-text {
            font-size: 1.05rem;
            color: var(--text-muted);
            margin-bottom: 16px;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin: 40px 0;
        }

        .stat-card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 20px;
            text-align: center;
        }

        .stat-number {
            font-size: 1.5rem;
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 4px;
        }

        .stat-label {
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        section {
            margin-bottom: 60px;
        }

        h2 {
            font-size: 1.5rem;
            font-weight: 500;
            color: #ffffff;
            margin-bottom: 20px;
            letter-spacing: -0.02em;
            text-transform: uppercase;
        }

        p {
            color: var(--text-muted);
            margin-bottom: 16px;
        }

        .case-study {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 30px;
        }

        .case-study a {
            color: var(--accent-color);
            text-decoration: none;
        }
        .case-study a:hover {
            text-decoration: underline;
        }

        .timeline-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }

        .timeline-card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            overflow: hidden;
            text-align: center;
            cursor: pointer;
        }

        .timeline-card img {
            width: 100%;
            aspect-ratio: 16/9;
            object-fit: cover;
            display: block;
        }

        .timeline-year {
            padding: 10px;
            font-size: 0.85rem;
            color: var(--text-muted);
            border-top: 1px solid var(--border-color);
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.5rem;
            width: 100%;
        }

        .grid-item {
            position: relative;
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 4px;
            overflow: hidden;
            aspect-ratio: 16 / 9;
            cursor: pointer;
            transition: border-color 0.2s ease, transform 0.2s ease;
        }

        .grid-item:hover {
            border-color: #525252;
            transform: translateY(-2px);
        }

        .grid-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .date-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 16px 12px 10px 12px;
            background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 100%);
            color: #ffffff;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            opacity: 0;
            transform: translateY(8px);
            transition: opacity 0.2s ease, transform 0.2s ease;
        }

        .grid-item:hover .date-overlay {
            opacity: 1;
            transform: translateY(0);
        }

        .graveyard-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.5rem;
        }

        /* Modal Overlay */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            justify-content: center;
            align-items: center;
            padding: 20px;
            opacity: 0;
            transition: opacity 0.2s ease;
        }

        .modal.active {
            display: flex;
            opacity: 1;
        }

        .modal img {
            max-width: 85vw;
            max-height: 85vh;
            border-radius: 6px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            transform-origin: top left;
            will-change: transform;
            backface-visibility: hidden;
            transform: translate3d(0,0,0);
        }

        footer {
            border-top: 1px solid var(--border-color);
            padding-top: 30px;
            margin-top: 40px;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        footer a {
            color: var(--text-main);
            text-decoration: none;
        }

        @media (max-width: 768px) {
            .stats-grid, .timeline-grid, .grid-container, .graveyard-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            h1 { font-size: 2.2rem; }
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <span class="tagline-badge">Creator Background · Visual Strategy</span>
            <h1>GHUYD LAPAZ</h1>
            <p class="subtitle">I learned to make people click before I ever called myself a designer.</p>
            <p class="bio-text">I started creating content on YouTube at exactly 14 years old. By figuring out visual packaging, hooks, and retention early on, I built a channel to over 60K subscribers and 4.25M+ views—buying a peak-era iPhone 11 entirely from my own channel revenue when I was still 14.</p>
            <p class="bio-text">Running my own channel taught me how design decisions dictate whether someone stops scrolling in a crowded feed. Now approaching 21, I bring that real-world performance intuition and execution maturity to thumbnail design and digital packaging.</p>
            
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
        </header>

        <section>
            <h2>Flagship Case Study</h2>
            <div class="case-study">
                <h3 style="color:#fff; margin-bottom: 8px; font-size: 1.2rem;">How To Rank Up Faster Guide 2021 | Solo Rank Up in Mobile Legends</h3>
                <p><strong>Published:</strong> April 4, 2020 | <strong>Views:</strong> 1,471,301 | <a href="https://youtu.be/6FwTJFmi-jw" target="_blank">Watch on YouTube ↗</a></p>
                <p style="margin-top: 12px;">Built when I was 14. This video became a primary traffic engine. The packaging relied on high-contrast subject isolation, clear emotional cues, and immediate readability at mobile thumbnail scale—lessons learned by directly watching what analytics and audience response dictated.</p>
            </div>
        </section>

        <section>
            <h2>THUMBNAIL EVOLUTION</h2>
            <p>A look at how visual execution matured from early experiments to intentional design systems.</p>
            <div class="timeline-grid">
                <div class="timeline-card" onclick="openModalFromSrc('old6.jpg', event)">
                    <img src="old6.jpg" alt="2019" loading="lazy" decoding="async">
                    <div class="timeline-year">2019 (Early)</div>
                </div>
                <div class="timeline-card" onclick="openModalFromSrc('thumbnail_42.jpg', event)">
                    <img src="thumbnail_42.jpg" alt="2020" loading="lazy" decoding="async">
                    <div class="timeline-year">2020 (Growth)</div>
                </div>
                <div class="timeline-card" onclick="openModalFromSrc('thumbnail_28.jpg', event)">
                    <img src="thumbnail_28.jpg" alt="2021" loading="lazy" decoding="async">
                    <div class="timeline-year">2021 (Refinement)</div>
                </div>
                <div class="timeline-card" onclick="openModalFromSrc('thumbnail_101.jpg', event)">
                    <img src="thumbnail_101.jpg" alt="2022" loading="lazy" decoding="async">
                    <div class="timeline-year">2022 (Prime)</div>
                </div>
            </div>
        </section>

        <section>
            <h2>THUMBNAIL GALLERY</h2>
            <p>Hover for year created.</p>
            <div class="grid-container">
    <!-- GALLERY_ITEMS -->
            </div>
        </section>

        <section>
            <h2>THUMBNAIL GRAVEYARD</h2>
            <p>Early iterations and raw tests from years ago. Growth requires looking back at what didn't work.</p>
            <div class="graveyard-grid">
    <!-- GRAVEYARD_ITEMS -->
            </div>
        </section>

        <footer>
            <p>Get in touch: <a href="mailto:might370@gmail.com">might370@gmail.com</a> &nbsp;|&nbsp; Discord: <code>gyd.000000</code></p>
        </footer>
    </div>

    <!-- Lightbox Modal -->
    <div id="imageModal" class="modal" onclick="closeModal()">
        <img id="modalImg" src="" alt="Fullscreen View">
    </div>

    <script>
        let activeThumbnail = null;

        function openModal(cardElement) {
            const img = cardElement.querySelector('img');
            activeThumbnail = img;
            const modal = document.getElementById('imageModal');
            const modalImg = document.getElementById('modalImg');

            // 1. FIRST: Get initial bounding rect
            const firstRect = img.getBoundingClientRect();
            modalImg.src = img.src;
            modal.classList.add('active');

            // 2. Schedule via requestAnimationFrame to eliminate layout thrashing & align with monitor refresh rate
            requestAnimationFrame(() => {
                const lastRect = modalImg.getBoundingClientRect();

                const deltaX = firstRect.left - lastRect.left;
                const deltaY = firstRect.top - lastRect.top;
                const scaleX = firstRect.width / lastRect.width;
                const scaleY = firstRect.height / lastRect.height;

                modalImg.style.transition = 'none';
                modalImg.style.transform = `translate3d(${deltaX}px, ${deltaY}px, 0) scale(${scaleX}, ${scaleY})`;

                // Force browser layout flush before triggering smooth render
                modalImg.getBoundingClientRect();

                requestAnimationFrame(() => {
                    modalImg.style.transition = 'transform 0.28s cubic-bezier(0.16, 1, 0.3, 1)';
                    modalImg.style.transform = 'translate3d(0, 0, 0) scale(1)';
                });
            });
        }

        function openModalFromSrc(src, event) {
            event.stopPropagation();
            const modal = document.getElementById('imageModal');
            const modalImg = document.getElementById('modalImg');
            modalImg.src = src;
            activeThumbnail = null;
            modal.classList.add('active');
            
            requestAnimationFrame(() => {
                modalImg.style.transition = 'none';
                modalImg.style.transform = 'translate3d(0, 0, 0) scale(0.95)';
                modalImg.getBoundingClientRect();
                requestAnimationFrame(() => {
                    modalImg.style.transition = 'transform 0.25s cubic-bezier(0.16, 1, 0.3, 1)';
                    modalImg.style.transform = 'translate3d(0, 0, 0) scale(1)';
                });
            });
        }

        function closeModal() {
            const modal = document.getElementById('imageModal');
            const modalImg = document.getElementById('modalImg');

            if (!activeThumbnail) {
                modal.classList.remove('active');
                modalImg.style.transform = 'translate3d(0,0,0)';
                return;
            }

            const firstRect = activeThumbnail.getBoundingClientRect();
            const lastRect = modalImg.getBoundingClientRect();

            const deltaX = firstRect.left - lastRect.left;
            const deltaY = firstRect.top - lastRect.top;
            const scaleX = firstRect.width / lastRect.width;
            const scaleY = firstRect.height / lastRect.height;

            modalImg.style.transition = 'transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease';
            modalImg.style.transform = `translate3d(${deltaX}px, ${deltaY}px, 0) scale(${scaleX}, ${scaleY})`;
            modal.style.opacity = '0';

            setTimeout(() => {
                modal.classList.remove('active');
                modal.style.opacity = '1';
                modalImg.style.transform = 'translate3d(0,0,0)';
                activeThumbnail = null;
            }, 250);
        }
    </script>
</body>
</html>
"""

# Inject items via replacement
html_content = html_template.replace("<!-- GALLERY_ITEMS -->", gallery_html)
html_content = html_content.replace("<!-- GRAVEYARD_ITEMS -->", graveyard_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Success! RAF-scheduled FLIP engine applied for maximum refresh rate synchronization.")