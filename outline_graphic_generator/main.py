import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap

# Outline with manual line breaks
"""
manual_outline = {
    "1. Einleitung": [
        "1.1 Hintergrund und\nMotivation",
        "1.2 Zielsetzung und\nForschungsfrage",
        "1.3 Gliederung der Arbeit"
    ],
    "2. Theoretische Grundlagen und verwandte Arbeiten": [
        "2.1 Design Science\nResearch",
        "2.2 Verwandte\nArbeiten",
        "2.3 Bargeldlose\nBezahlsysteme",
        "2.4 Self-Service-\nTechnologien",
        "2.5 Web-\nFrameworks",
    ],
    "3. Methodik": [
        "3.1 Forschungsdesign",
        "3.2 Vorgehen in den Projektphasen"
    ],
    "4. Ergebnisse": [
        "4.1 Anforderungsanalyse",
        "4.2 Systemarchitektur\nund Design",
        "4.3 Implementierung und\nIntegration"
    ],
    "5. Evaluation": [
        "5.1 Technische Evaluation",
        "5.2 Nutzerzentrierte Evaluation",
        "5.3 Schlussfolgerung"
    ],
    "6. Diskussion": [
        "6.1 Limitationen der\nArbeit",
        "6.2 Beantwortung der\nForschungsfrage",
        "6.3 Einordnung in den\nKontext des Design\nScience Research",
        "6.4 Lessons Learned"
    ],
    "7. Zusammenfassung und Ausblick": [
        "7.1 Zusammenfassung der\nErgebnisse",
        "7.2 Ausblick auf zukünftige\nForschungsrichtungen",
        "7.3 Schlusswort"
    ]
}
"""

manual_outline = {
    "1. Einleitung": [
    ],
    "2. Grundlagen und verwandte Arbeiten": [
        "2.1 Design Science Research",
        "2.2 Verwandte Arbeiten",
        "2.3 Weitere Grundlagen",
    ],
    "3. Methodik": [
        "3.1 Forschungsdesign",
        "3.2 Vorgehen in den Projektphasen"
    ],
    "4. Ergebnisse": [
        "4.1 Anforderungsanalyse",
        "4.2 Systemarchitektur\nund Design",
        "4.3 Implementierung und\nIntegration"
    ],
    "5. Evaluation": [
        "5.1 Technische Evaluation",
        "5.2 Nutzerzentrierte Evaluation",
        "5.3 Schlussfolgerung"
    ],
    "6. Diskussion": [
        "6.1 Limitationen",
        "6.2 Beantwortung der\nForschungsfrage",
        "6.3 Einordnung in den\nKontext des DSR",
        "6.4 Lessons Learned"
    ],
    "7. Zusammenfassung und Ausblick": [
        "7.1 Zusammenfassung der\nErgebnisse",
        "7.2 Ausblick auf zukünftige\nForschungsrichtungen",
        "7.3 Schlusswort"
    ]
}

# Re-plot with more compact boxes while maintaining spacing
fig, ax = plt.subplots(figsize=(14, 12))  # Increase height of the figure to accommodate larger boxes
plt.axis('off')
y = 0
main_box_width = 13  # Increased width for main chapter boxes to enclose subchapter boxes with a margin

# Generate boxes with compact heights and maintained spacing
for main, subs in manual_outline.items():
    # Calculate maximum height for subchapter boxes
    max_height = 0.5
    max_breaks = 0
    for sub in subs:
        breaks = sub.count('\n')
        if breaks > max_breaks:
            max_breaks = breaks
    max_height += max_breaks*0.25
    if len(subs) == 0:
        max_height = 0
        text_offset = 0.1
    else:
        text_offset = 0

    height = 0.5  # Reduce space between the title and the small boxes
    dy = max_height + 0.1  # Slightly reduce extra height for spacing between subchapter boxes
    width = main_box_width  # Use fixed width for consistency

    # Main chapter box
    main_box = patches.Rectangle((-0.1, y), width + 0.2, height + dy + 0.1, linewidth=1, edgecolor='black',
                                 facecolor='none')
    ax.add_patch(main_box)
    ax.text(width / 2, y + 0.15 + text_offset, main, horizontalalignment='center', verticalalignment='top', fontsize=12, weight='bold')

    # Subchapter boxes with spacing
    try:
        sub_width = (width - 0.2 - (0.2 * (len(subs) - 1))) / len(
            subs)  # Adjust subchapter box width to account for spacing
        sub_x = 0
        for sub in subs:
            sub_box = patches.Rectangle((sub_x + 0.1, y + height), sub_width, max_height, linewidth=1, edgecolor='black',
                                        facecolor='none')
            ax.add_patch(sub_box)
            ax.text(sub_x + sub_width / 2 + 0.1, y + height + max_height / 2, sub, horizontalalignment='center',
                    verticalalignment='center', fontsize=12, wrap=True)
            sub_x += sub_width + 0.2  # Add spacing between subchapter boxes

        y += height + dy + 0.3  # Slightly reduce spacing between main sections
    except ZeroDivisionError:
        y += height + dy + 0.3



ax.set_xlim(-0.5, width + 0.5)
ax.set_ylim(0, y)
plt.gca().invert_yaxis()

plt.savefig('thesis_structure.png', bbox_inches='tight', dpi=300)
#plt.show()