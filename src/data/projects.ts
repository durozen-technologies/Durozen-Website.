export interface ProjectItem {
  id: string;
  name: string;
  category: 'Automotive' | 'Beauty' | 'Healthcare' | 'Lifestyle' | 'Hospitality';
  tagline: string;
  description: string;
  url: string;
  accentColor: string; // DUROZEN Red, Yellow, Green, or Blue
  accentBadge: string;
  year: string;
  tags: string[];
  client: string;
  highlights: string[];
  domain: string;
  imageUrl?: string; // Custom website front look picture / screenshot
}

export const LIVE_PROJECTS: ProjectItem[] = [
  // 1. Makeover Studio
  {
    id: 'makeover',
    name: 'Makeover Studio',
    category: 'Beauty',
    tagline: 'Luxury makeup, beauty styling & personal makeover destination',
    description: 'A chic, high-fashion makeover and beauty consultation platform showcasing artist portfolios, transformation lookbooks, and customized packages.',
    url: 'https://makeeeover.netlify.app',
    accentColor: '#FACC15', // DUROZEN Yellow
    accentBadge: 'Beauty',
    year: '2026',
    tags: ['Beauty Styling', 'Lookbook', 'Personal Makeover', 'Live Website'],
    client: 'Makeover Studio',
    highlights: ['Transformation Gallery', 'Artist Booking', 'Custom Packages'],
    domain: 'makeeeover.netlify.app',
    imageUrl: '/screenshots/makeover.jpg'
  },
  // 2. Eye Hospital
  {
    id: 'eye-hospital',
    name: 'Eye Hospital',
    category: 'Healthcare',
    tagline: 'Advanced ophthalmology clinic, laser vision & surgical care',
    description: 'An institutional healthcare portal for eye care, cataract surgery, and retinal treatments featuring specialist directories and online appointment booking.',
    url: 'https://eyehospital1.netlify.app',
    accentColor: '#22C55E', // DUROZEN Green
    accentBadge: 'Healthcare',
    year: '2026',
    tags: ['Ophthalmology', 'Doctor Directory', 'Appointment Booking', 'Live Website'],
    client: 'Apex Eye Hospital',
    highlights: ['Specialist Profiles', 'Online Appointment Booking', 'Surgical Guides'],
    domain: 'eyehospital1.netlify.app',
    imageUrl: '/screenshots/eye-hospital.jpg'
  },
  // 3. Salon Studio
  {
    id: 'salon',
    name: 'Salon Studio',
    category: 'Beauty',
    tagline: 'Premium hair styling, spa therapies & grooming experience',
    description: 'A contemporary salon web experience with service menus, pricing tiers, hair stylist selection, and automated slot reservations.',
    url: 'https://salonn1.netlify.app',
    accentColor: '#E52521', // DUROZEN Red
    accentBadge: 'Beauty',
    year: '2026',
    tags: ['Hair & Spa', 'Service Menu', 'Slot Booking', 'Live Website'],
    client: 'Urban Salon Studio',
    highlights: ['Slot Reservation', 'Tiered Service Menu', 'Stylist Portfolio'],
    domain: 'salonn1.netlify.app',
    imageUrl: '/screenshots/salon.jpg'
  },
  // 4. MMR Motor
  {
    id: 'mmr-motor',
    name: 'MMR Motor',
    category: 'Automotive',
    tagline: 'Modern two-wheeler sales, maintenance & spare parts portal',
    description: 'A full-service two-wheeler automotive platform featuring interactive bike models, service booking schedules, and genuine spare parts catalog.',
    url: 'https://mmrmotor.netlify.app',
    accentColor: '#E52521', // DUROZEN Red
    accentBadge: 'Automotive',
    year: '2026',
    tags: ['Automotive', 'Bike Service', 'Parts Catalog', 'Live Website'],
    client: 'MMR Motor Hub',
    highlights: ['Instant Service Booking', 'Multi-Brand Catalog', 'Mobile First'],
    domain: 'mmrmotor.netlify.app',
    imageUrl: '/screenshots/mmr-motor.jpg'
  },
  // 5. Scootyy
  {
    id: 'scootyy',
    name: 'Scootyy',
    category: 'Automotive',
    tagline: 'Smart electric scooter rental, test drives & urban mobility',
    description: 'An eco-friendly electric scooter showcase featuring battery specs, range estimators, online test drive reservations, and urban dealership locators.',
    url: 'https://scootyy.netlify.app',
    accentColor: '#2563EB', // DUROZEN Blue
    accentBadge: 'Automotive',
    year: '2026',
    tags: ['EV Mobility', 'Scooter Rental', 'Test Drive UI', 'Live Website'],
    client: 'Scootyy Urban Mobility',
    highlights: ['Range Calculator', 'Test Ride Scheduler', 'Interactive Fleet'],
    domain: 'scootyy.netlify.app',
    imageUrl: '/screenshots/scootyy.jpg'
  },
  // 6. Bridal Makeover
  {
    id: 'bridal',
    name: 'Bridal Makeover',
    category: 'Beauty',
    tagline: 'Bespoke bridal makeover, couture beauty & wedding glam packages',
    description: 'An ethereal bridal platform highlighting wedding day looks, mehendi and reception styling packages, and client testimonial showcases.',
    url: 'https://bridall.netlify.app',
    accentColor: '#FACC15', // DUROZEN Yellow
    accentBadge: 'Beauty',
    year: '2026',
    tags: ['Bridal Glam', 'Couture Styling', 'Wedding Lookbook', 'Live Website'],
    client: 'Bridal Makeover Atelier',
    highlights: ['Wedding Day Lookbook', 'Bridal Consultations', 'Package Customizer'],
    domain: 'bridall.netlify.app',
    imageUrl: '/screenshots/bridal-makeover.jpg'
  },
  // 7. Eye Care Center
  {
    id: 'eye-care',
    name: 'Eye Care Center',
    category: 'Healthcare',
    tagline: 'Comprehensive optical diagnostics, contact lenses & eyewear',
    description: 'A modern vision care and optical dispensary website providing eye examinations, designer frames gallery, and prescription renewal support.',
    url: 'https://eyecareee.netlify.app',
    accentColor: '#22C55E', // DUROZEN Green
    accentBadge: 'Healthcare',
    year: '2026',
    tags: ['Optometry', 'Eyewear Gallery', 'Vision Check', 'Live Website'],
    client: 'Vision Eye Care Center',
    highlights: ['Vision Check Guidance', 'Eyewear Catalog', 'Prescription Care'],
    domain: 'eyecareee.netlify.app',
    imageUrl: '/screenshots/eye-care.jpg'
  },
  // 8. Nurserie Plant
  {
    id: 'nurserie-plant',
    name: 'Nurserie Plant',
    category: 'Lifestyle',
    tagline: 'Botanical nursery, exotic indoor plants & landscape greens',
    description: 'A vibrant gardening and botanical nursery website showcasing rare indoor houseplants, bonsai trees, organic soils, and plant care instructions.',
    url: 'https://nurserieplant.netlify.app/',
    accentColor: '#22C55E', // DUROZEN Green
    accentBadge: 'Lifestyle',
    year: '2026',
    tags: ['Botanical Nursery', 'Houseplants', 'Garden Greens', 'Live Website'],
    client: 'Nurserie Botanical Greens',
    highlights: ['Plant Care Guides', 'Rare Species Catalog', 'Gardening Supplies'],
    domain: 'nurserieplant.netlify.app',
    imageUrl: '/screenshots/nurserie-plant.jpg'
  },
  // 9. Resort Getaway
  {
    id: 'resort',
    name: 'Resort Getaway',
    category: 'Hospitality',
    tagline: 'Luxury vacation retreat, villas, private dining & wellness spa',
    description: 'An immersive hospitality experience presenting luxury villa accommodations, beachfront suites, dining menus, and direct online suite booking.',
    url: 'https://resortt2.netlify.app/',
    accentColor: '#2563EB', // DUROZEN Blue
    accentBadge: 'Hospitality',
    year: '2026',
    tags: ['Luxury Resort', 'Villa Booking', 'Dining & Spa', 'Live Website'],
    client: 'Azure Bay Luxury Resort',
    highlights: ['Direct Room Booking', 'Virtual Villa Tour', 'Spa Packages'],
    domain: 'resortt2.netlify.app',
    imageUrl: '/screenshots/resort.jpg'
  },
  // 10. MMR Motors
  {
    id: 'mmr-motors',
    name: 'MMR Motors',
    category: 'Automotive',
    tagline: 'Premium pre-owned cars, vehicle trade-ins & certified auto dealership',
    description: 'A comprehensive automotive dealership platform with certified pre-owned vehicle listings, EMI financing calculators, and instant test drive bookings.',
    url: 'https://mmrmotors.uk',
    accentColor: '#E52521', // DUROZEN Red
    accentBadge: 'Automotive',
    year: '2026',
    tags: ['Pre-Owned Cars', 'Auto Dealership', 'EMI Calculator', 'Live Website'],
    client: 'MMR Motors Dealership',
    highlights: ['Certified Inventory', 'Auto Financing Calculator', 'Instant Vehicle Inspection'],
    domain: 'mmrmotors.uk',
    imageUrl: '/screenshots/mmr-motors.jpg'
  }
];

// Alias for backwards compatibility if needed
export const INITIAL_PROJECTS = LIVE_PROJECTS;
