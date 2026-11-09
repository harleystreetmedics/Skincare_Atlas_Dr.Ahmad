const SKIN_CONCERNS = [
  {id:"all", label:"All concerns", detail:"Explore the skin treatments listed by Harley Street Aesthetics. A clinician decides which, if any, is suitable."},
  {id:"pigment", label:"Pigmentation & melasma", detail:"Brown marks can have different causes. Melasma, sun spots and marks after acne may need different plans."},
  {id:"breakouts", label:"Breakouts & congestion", detail:"For oily, blocked or acne-prone skin, discuss the skin condition first and then whether a procedure adds value."},
  {id:"texture", label:"Texture & acne marks", detail:"Shallow uneven texture and deeper acne scars respond differently. An assessment helps set realistic goals."},
  {id:"redness", label:"Redness & thread veins", detail:"Persistent redness and visible vessels need a skin-type check. Light treatment is not suitable for everyone."},
  {id:"glow", label:"Dullness & hydration", detail:"Dryness, dullness and uneven surface texture can overlap. The useful first step may be a simpler routine."},
  {id:"pores", label:"Oil & visible pores", detail:"Pores cannot be removed. Treatment may help their appearance by addressing oiliness or surrounding texture."},
  {id:"firmness", label:"Fine lines & firmness", detail:"Skin quality and facial structure are different concerns. Discuss what change a treatment can realistically make."}
];

const SKIN_TREATMENTS = [
  {
    name:"Signature Pigmentation Programme",
    image:"assets/photos/treatment-pigmentation.webp",
    imageAlt:"Clinician assessing facial pigmentation",
    type:"Tone",
    concerns:["pigment"],
    summary:"A clinician-planned, needle-free programme for flat facial pigmentation and uneven tone.",
    note:"The cause of a mark must be assessed first. Melasma often needs long-term care.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/pigmentation",
    guide:2
  },
  {
    name:"Virtue RF Needling",
    image:"assets/photos/treatment-rf-needling.webp",
    imageAlt:"RF needling handpiece held against the cheek",
    type:"Texture",
    concerns:["texture","pores","firmness"],
    summary:"Fine needles deliver radiofrequency energy beneath the surface. It may be discussed for acne scars, texture, pores and early laxity.",
    note:"Device settings, skin tone, healing and risks need an individual review.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/virtue-rf",
    guide:7
  },
  {
    name:"Carbon Laser Facial",
    image:"assets/photos/treatment-carbon-laser.webp",
    imageAlt:"Carbon lotion being applied to the cheek",
    type:"Oil & glow",
    concerns:["breakouts","glow","pores"],
    summary:"A carbon lotion and laser are used for oily skin, visible pores, dullness and mild acne-prone skin.",
    note:"It is not a substitute for assessment of active acne or deeper scarring.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/carbon-laser-facial",
    guide:9
  },
  {
    name:"IPL Facial",
    image:"assets/photos/treatment-ipl.webp",
    imageAlt:"IPL handpiece and protective eyewear during a facial",
    type:"Redness & sun spots",
    concerns:["redness","pigment"],
    summary:"Filtered light can target visible redness, thread veins and selected sun-induced brown spots.",
    note:"IPL is not appropriate for every skin tone or type of pigmentation. Melasma needs particular care.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/ipl-facial",
    guide:9
  },
  {
    name:"Chemical Peels",
    image:"assets/photos/treatment-chemical-peels.webp",
    imageAlt:"A peel solution being applied with a brush",
    type:"Resurfacing",
    concerns:["breakouts","pigment","texture","glow"],
    summary:"A clinician selects the peel and depth for concerns such as congestion, dullness, uneven tone or fine lines.",
    note:"Preparation, skin tone and peel depth affect recovery and pigment risk.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/chemical-peels",
    guide:8
  },
  {
    name:"Chemical Peel + Mesotherapy",
    image:"assets/photos/treatment-peel-mesotherapy.webp",
    imageAlt:"Clinician preparing mesotherapy materials",
    type:"Renew & hydrate",
    concerns:["glow","texture"],
    summary:"A selected peel is followed by mesotherapy for surface renewal and hydration.",
    note:"The two steps and their aftercare should be planned for your skin.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/peel-mesotherapy",
    guide:8
  },
  {
    name:"VI Peel",
    image:"assets/photos/treatment-vi-peel.webp",
    imageAlt:"A peel solution being applied to the cheek",
    type:"Resurfacing",
    concerns:["pigment","breakouts","texture"],
    summary:"A named medical-grade peel considered for uneven tone, acne-prone skin and surface texture.",
    note:"Visible peeling and a take-home aftercare routine are part of the process.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/vi-peel",
    guide:8
  },
  {
    name:"Cosmelan Peel",
    image:"assets/photos/treatment-cosmelan.webp",
    imageAlt:"A pigmentation mask being applied to the cheek",
    type:"Pigmentation",
    concerns:["pigment"],
    summary:"An in-clinic depigmentation mask followed by a structured home-care programme for concerns including melasma.",
    note:"This is a longer programme. Pigment can return, so maintenance and sun protection matter.",
    url:"https://harleystreetaesthetic.co.uk/london/treatments/cosmelan-peel",
    guide:2
  }
];
