# **Design System: Utilitarian Terminal (ERP/Ledger Interface)**

## **1\. Visual Theme & Atmosphere**

A hyper-functional, keyboard-first terminal interface. The atmosphere is **Cockpit Dense (10)**, **Predictable Symmetric (1)**, and **Static Restrained (1)**. It champions raw data density and instant power-user operation over aesthetic breathing room. It feels like a high-precision industrial tool—clinical, structured, and entirely devoid of decorative fluff.

## **2\. Color Palette & Roles**

* **Terminal Slate** (\#172026) — Top navigation header, primary active text.  
* **Industrial Grey** (\#BCC3C8) — Main canvas background, inactive workspace backdrop.  
* **Ledger White** (\#F8F9FA) — Active data panel backgrounds and list containers.  
* **Input Cream** (\#FEFBEA) — Specific background fill for active text inputs (nostalgic, high-contrast focus indicator).  
* **Structural Blue** (\#2E5085) — List headers, tight structural borders, and active panel outlines.  
* **Operator Amber** (\#F5B935) — **\[ACCENT\]** The single accent color. Used strictly for the active selection row in lists and critical focus rings. Maximum contrast against Slate text.  
  *(Max 1 accent. Saturation tightly controlled. Pure black is banned; use Terminal Slate.)*

## **3\. Typography Rules**

* **Display/UI Labels:** Geist — Medium weight, compact tracking. Sized small (12px–14px) with extremely tight leading (1.2) to maximize vertical screen real estate.  
* **Data/Numbers (Mandatory):** JetBrains Mono — Every single number, date, keyboard shortcut, and tabular data entry MUST use this monospace font for perfect vertical alignment.  
* **Keyboard Shortcuts:** Must be visually distinct. Use an underline on the specific trigger letter (e.g., \<u\>K\</u\>: Company) or a subtle font-weight change.  
* **Banned:** Inter, all Serif fonts, and generic system fonts. No large "hero" typography allowed.

## **4\. Component Stylings**

* **Lists/Data Tables:** The core UI element. Zebra striping is banned. The active/focused row receives a full Operator Amber background fill with Terminal Slate text. Inactive rows are transparent.  
* **Inputs:** Sharp corners (0px to 2px max radius). Input Cream background. Hard 1px Structural Blue border. No focus shadows, only a rigid 2px outline.  
* **Cards/Modals:** 0px border radius. Hard 1px Structural Blue border. Zero drop shadows—use full page dimming (overlay) or stark contrast against Industrial Grey to indicate elevation. Top title bar must be Ledger White with Structural Blue text and borders.  
* **Buttons:** Purely flat. Embedded within top or bottom navigation bars. No standalone floating primary buttons.

## **5\. Layout Principles**

* **Strict Viewport Containment:** Full viewport utilization (min-h-\[100dvh\]). No page-level vertical scrolling. All scrolling must be contained strictly within internal list components.  
* **Rigid Framing:** Fixed top utility bar (dark). Fixed bottom status/action bar (light).  
* **Central Modality:** Primary tasks (like "Select Company") appear as absolute-centered, rigidly defined panels overlapping the Industrial Grey background.  
* **Zero Decorative Whitespace:** Use margin/padding purely for technical separation (2px–8px gaps max). Data density is the highest priority.  
* **CSS Grid:** Use strict grid templates for list headers and rows to ensure 1:1 column alignment.

## **6\. Motion & Interaction**

* **Instantaneous Snapping:** No cinematic choreographies. Power users require instant feedback.  
* **Ultra-Stiff Physics:** For any necessary transitions (like modal appearances), use exceptionally stiff spring physics (stiffness: 400, damping: 40\) so it feels immediate but polished.  
* **Hover States:** Instant background color change. Zero fade-in duration.  
* **Keyboard Navigation:** Visual state changes for arrow-key navigation must be instantaneous and highly visible (Operator Amber row highlight).

## **7\. Anti-Patterns (Banned)**

* **NEVER** use rounded corners greater than 2px. This is an industrial tool.  
* **NEVER** use drop shadows, elevation blurs, or glow effects.  
* **NEVER** use Inter, emojis, or serif fonts.  
* **NEVER** introduce overlapping elements outside of the strict centered-modal architecture.  
* **NEVER** add "breathing room" or large padding—do not dilute the data density.  
* **NEVER** use pure black (\#000000).  
* **NEVER** use AI copywriting clichés ("Elevate", "Seamless", "Unleash"). Use strict utilitarian nouns ("Company", "Data", "Exchange").