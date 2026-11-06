import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { OpeningScreen } from './components/OpeningScreen';
import { PortfolioHome } from './components/PortfolioHome';
import { ProjectsPage } from './components/ProjectsPage';
import { AboutPage } from './components/AboutPage';
import { ContactPage } from './components/ContactPage';
import { AdminPortal } from './components/AdminPortal';
import { ProjectQuickViewModal } from './components/ProjectQuickViewModal';
import { ProjectItem } from './data/projects';

export default function App() {
  // Current route pathname: '/' | '/projects' | '/about' | '/contact' | '/admin'
  const [currentPath, setCurrentPath] = useState<string>(() => {
    if (typeof window !== 'undefined') {
      const path = window.location.pathname.toLowerCase().replace(/\/+$/, '') || '/';
      const hash = window.location.hash.toLowerCase();
      if (path === '/admin' || path.startsWith('/admin') || hash.includes('admin')) {
        return '/admin';
      }
      return path;
    }
    return '/';
  });

  // Entrance & Opening screen states
  const [hasEnteredPortfolio, setHasEnteredPortfolio] = useState<boolean>(() => {
    if (typeof window !== 'undefined') {
      const path = window.location.pathname.toLowerCase().replace(/\/+$/, '') || '/';
      // If user directly navigates to a subpage, enter immediately
      if (path !== '/' && path !== '') return true;
    }
    return false;
  });

  const [showOpeningScreen, setShowOpeningScreen] = useState<boolean>(() => {
    if (typeof window !== 'undefined') {
      const path = window.location.pathname.toLowerCase().replace(/\/+$/, '') || '/';
      if (path !== '/' && path !== '') return false;
    }
    return true;
  });

  const [openingKey, setOpeningKey] = useState(0);
  const [adminPreviewProject, setAdminPreviewProject] = useState<ProjectItem | null>(null);

  // Client-side Navigation helper
  const navigate = (path: string) => {
    const cleanPath = path.toLowerCase().replace(/\/+$/, '') || '/';
    if (window.location.pathname.toLowerCase().replace(/\/+$/, '') !== cleanPath) {
      window.history.pushState({}, '', cleanPath);
    }
    setCurrentPath(cleanPath);
    setHasEnteredPortfolio(true);
    setShowOpeningScreen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Sync popstate (browser back/forward) and shortcut (Ctrl + Alt + A)
  useEffect(() => {
    const handleLocationChange = () => {
      const path = window.location.pathname.toLowerCase().replace(/\/+$/, '') || '/';
      const hash = window.location.hash.toLowerCase();
      if (path === '/admin' || path.startsWith('/admin') || hash.includes('admin')) {
        setCurrentPath('/admin');
      } else {
        setCurrentPath(path);
      }
      setHasEnteredPortfolio(true);
      setShowOpeningScreen(false);
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      // Secret Admin Shortcut: Ctrl + Alt + A
      if ((e.ctrlKey || e.metaKey) && e.altKey && (e.key === 'a' || e.key === 'A')) {
        e.preventDefault();
        navigate('/admin');
      }
    };

    window.addEventListener('popstate', handleLocationChange);
    window.addEventListener('hashchange', handleLocationChange);
    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('popstate', handleLocationChange);
      window.removeEventListener('hashchange', handleLocationChange);
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  const handleExplore = () => {
    setHasEnteredPortfolio(true);
    setShowOpeningScreen(false);
  };

  const handleReplayIntro = () => {
    navigate('/');
    setShowOpeningScreen(true);
    setHasEnteredPortfolio(false);
    setOpeningKey(prev => prev + 1);
  };

  // If in Admin view, render Admin Portal
  if (currentPath === '/admin' || currentPath.startsWith('/admin')) {
    return (
      <main className="min-h-screen bg-slate-50 font-sans antialiased">
        <AdminPortal 
          onBackToPortfolio={() => navigate('/')}
          onPreviewProject={(project) => setAdminPreviewProject(project)}
        />

        {/* Quick View Modal for Admin Preview */}
        <ProjectQuickViewModal
          project={adminPreviewProject}
          onClose={() => setAdminPreviewProject(null)}
        />
      </main>
    );
  }

  // Render appropriate public page
  const renderPage = () => {
    switch (currentPath) {
      case '/projects':
        return <ProjectsPage onNavigate={navigate} />;
      case '/about':
        return <AboutPage onNavigate={navigate} />;
      case '/contact':
        return <ContactPage onNavigate={navigate} />;
      case '/':
      default:
        return (
          <PortfolioHome 
            onNavigate={navigate}
            onReplayIntro={handleReplayIntro} 
            onOpenAdmin={() => navigate('/admin')}
          />
        );
    }
  };

  return (
    <main className="relative min-h-screen bg-white font-sans antialiased">
      {/* 1. The Active Page View */}
      <div 
        className={`transition-opacity duration-200 ${
          hasEnteredPortfolio ? 'opacity-100' : 'opacity-0 pointer-events-none'
        }`}
      >
        {renderPage()}
      </div>

      {/* 2. Original DUROZEN Logo Physics Drop Opening Screen (Home entrance) */}
      <AnimatePresence mode="wait">
        {showOpeningScreen && (
          <motion.div
            key={openingKey}
            initial={{ opacity: 1 }}
            exit={{ 
              opacity: 0,
              scale: 1.02,
              transition: { duration: 0.18, ease: 'easeOut' } 
            }}
            className="fixed inset-0 z-50 overflow-hidden"
          >
            <OpeningScreen onExplore={handleExplore} />
          </motion.div>
        )}
      </AnimatePresence>
    </main>
  );
}
