#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
███████╗███╗   ███╗ ██████╗ █████╗     ███████╗███╗   ███╗ █████╗ ██╗██╗     ██╗     ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝██╔══██╗    ██╔════╝████╗ ████║██╔══██╗██║██║     ██║    ██╔═══██╗██╔════╝ ██║  ██║██╔════╝██╔══██╗
█████╗  ██╔████╔██║██║     ███████║    █████╗  ██╔████╔██║███████║██║██║     ██║    ██║   ██║██║  ███╗███████║█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██║     ██╔══██║    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║    ██║   ██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║╚██████╗██║  ██║    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗██║    ╚██████╔╝╚██████╔╝██║  ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                           
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                                                                                                                         ▓
▓  ███╗   ███╗███████╗ ██████╗  █████╗     ███████╗███╗   ███╗ █████╗ ██╗██╗     ██████╗  ██████╗ ██╗  ██╗███████╗██████╗  ▓
▓  ████╗ ████║██╔════╝██╔════╝ ██╔══██╗    ██╔════╝████╗ ████║██╔══██╗██║██║     ██╔══██╗██╔════╝ ██║  ██║██╔════╝██╔══██╗ ▓
▓  ██╔████╔██║█████╗  ██║  ███╗███████║    █████╗  ██╔████╔██║███████║██║██║     ██║  ██║██║  ███╗███████║█████╗  ██████╔╝ ▓
▓  ██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║    ██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██║  ██║██║   ██║██╔══██║██╔══╝  ██╔══██╗ ▓
▓  ██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║    ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗██████╔╝╚██████╔╝██║  ██║███████╗██║  ██║ ▓
▓  ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ▓
▓                                                                                                                         ▓
▓  ██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗ █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗                ▓
▓  ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║                ▓
▓  ██║██╔██╗ ██║███████╗   ██║   ███████║██╔██╗ ██║   ██║   ███████║██║        ██║   ██║██║   ██║██╔██╗ ██║                ▓
▓  ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║   ██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║                ▓
▓  ██║██║ ╚████║███████║   ██║   ██║  ██║██║ ╚████║   ██║   ██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║                ▓
▓  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                ▓
▓                                                                                                                         ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
"""

import requests
import time
import json
import random
import sys
import os
import re
import hashlib
import threading
import socket
import ssl
import subprocess
import csv
import sqlite3
import asyncio
import aiohttp
import smtplib
import dns.resolver
import ipaddress
import urllib3
import warnings
import platform
import psutil
from datetime import datetime, timedelta
from urllib.parse import urlparse, quote, parse_qs
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from colorama import init, Fore, Back, Style
from typing import List, Dict, Tuple, Optional, Set, Any
from dataclasses import dataclass
from enum import Enum
import logging
from logging.handlers import RotatingFileHandler
from tqdm import tqdm
import pickle
import zlib
import base64
from cryptography.fernet import Fernet
import secrets
from fake_useragent import UserAgent
import whois
import xml.etree.ElementTree as ET
import html
from bs4 import BeautifulSoup
import brotli
import gzip

# ========== SUPPRESS WARNINGS ==========
warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ========== ENHANCED AUTO INSTALL DEPENDENCIES ==========
def install_package(package):
    """Install Python package silently"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
        return True
    except:
        return False

REQUIRED_PACKAGES = [
    "colorama", "requests", "dnspython", "fake-useragent", "tqdm", 
    "cryptography", "psutil", "aiohttp", "beautifulsoup4", "whois",
    "brotli", "python-whois"
]

print(f"{Fore.CYAN}[*] Checking dependencies...{Style.RESET_ALL}")
for package in REQUIRED_PACKAGES:
    try:
        if package == "colorama":
            from colorama import init, Fore, Back, Style
        elif package == "requests":
            import requests
        elif package == "dnspython":
            import dns.resolver
        elif package == "fake-useragent":
            from fake_useragent import UserAgent
        elif package == "tqdm":
            from tqdm import tqdm
        elif package == "cryptography":
            from cryptography.fernet import Fernet
        elif package == "psutil":
            import psutil
        elif package == "aiohttp":
            import aiohttp
        elif package == "beautifulsoup4":
            from bs4 import BeautifulSoup
        elif package == "whois":
            import whois
        elif package == "brotli":
            import brotli
    except ImportError:
        print(f"{Fore.YELLOW}[!] Installing {package}...{Style.RESET_ALL}")
        install_package(package)

init(autoreset=True)

# ========== ENHANCED CONFIGURATION ==========
@dataclass
class UltraConfig:
    # Version info
    VERSION: str = "ULTRA VIP 7.0"
    AUTHOR: str = "MR DUYKA"
    CONTACT: str = "github.com/duyuyd"
    RELEASE_DATE: str = "2024-01-01"
    
    # Performance
    MAX_WORKERS: int = 25
    MAX_PROCESSES: int = 4
    TIMEOUT: int = 30
    MAX_RETRIES: int = 5
    DELAY_BETWEEN_REQUESTS: float = 0.1
    DELAY_BETWEEN_EMAILS: float = 0.5
    CONCURRENT_CHECKS: int = 10
    
    # Cache
    CACHE_EXPIRE_HOURS: int = 168  # 7 days
    MAX_CACHE_SIZE: int = 50000
    COMPRESS_CACHE: bool = True
    
    # Security
    ROTATE_PROXY_EVERY: int = 15
    MAX_REQUESTS_PER_PROXY: int = 200
    ENABLE_ENCRYPTION: bool = True
    ENCRYPTION_KEY: str = None
    
    # Files
    DB_FILE: str = "mega_database_v2.db"
    CACHE_FILE: str = "mega_cache_v2.dat"
    RESULTS_FILE: str = "mega_results_v2.txt"
    PROXIES_FILE: str = "proxies.txt"
    EMAILS_FILE: str = "emails.txt"
    CONFIG_FILE: str = "mega_config_v2.json"
    STATS_FILE: str = "mega_stats_v2.json"
    LOG_FILE: str = "mega_checker.log"
    BACKUP_DIR: str = "backups"
    
    # API Keys (can be loaded from environment)
    HIBP_API_KEY: str = ""
    EMAILREP_API_KEY: str = ""
    
    # Advanced Settings
    ENABLE_AI_DETECTION: bool = False
    USE_TOR_PROXY: bool = False
    TOR_PROXY: str = "socks5://127.0.0.1:9050"
    ENABLE_GEOIP: bool = False
    CHECK_BREACHES: bool = True
    CHECK_PASSWORD_STRENGTH: bool = False
    
    # Colors
    COLORS: Dict = None
    
    def __post_init__(self):
        self.COLORS = {
            "success": Fore.GREEN,
            "error": Fore.RED,
            "warning": Fore.YELLOW,
            "info": Fore.CYAN,
            "highlight": Fore.MAGENTA,
            "debug": Fore.WHITE,
            "critical": Fore.RED + Style.BRIGHT,
            "notice": Fore.BLUE,
            "premium": Fore.YELLOW + Style.BRIGHT
        }
        
        if self.ENCRYPTION_KEY is None:
            key_file = ".encryption_key"
            if os.path.exists(key_file):
                with open(key_file, 'rb') as f:
                    self.ENCRYPTION_KEY = f.read()
            else:
                self.ENCRYPTION_KEY = Fernet.generate_key()
                with open(key_file, 'wb') as f:
                    f.write(self.ENCRYPTION_KEY)
                os.chmod(key_file, 0o600)

# ========== ENHANCED LOGGING SYSTEM ==========
class EnhancedLogger:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger('MegaChecker')
        self.logger.setLevel(logging.DEBUG)
        
        # Create handlers
        fh = RotatingFileHandler(
            config.LOG_FILE,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5
        )
        ch = logging.StreamHandler()
        
        # Create formatters
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
        self.logger.info(f"Mega Email Checker {config.VERSION} started")
    
    def log(self, level, message, color=None):
        """Log message with color"""
        log_method = {
            'debug': self.logger.debug,
            'info': self.logger.info,
            'warning': self.logger.warning,
            'error': self.logger.error,
            'critical': self.logger.critical
        }.get(level, self.logger.info)
        
        log_method(message)
        
        if color:
            print(f"{color}[{level.upper()}] {message}{Style.RESET_ALL}")
        else:
            colors = self.config.COLORS
            color_map = {
                'debug': colors['debug'],
                'info': colors['info'],
                'warning': colors['warning'],
                'error': colors['error'],
                'critical': colors['critical']
            }
            print(f"{color_map.get(level, colors['info'])}[{level.upper()}] {message}{Style.RESET_ALL}")

# ========== ENHANCED EMAIL VALIDATOR ==========
class EnhancedEmailValidator:
    def __init__(self):
        self.disposable_domains = self._load_disposable_domains()
        self.typo_domains = {
            'gmial.com': 'gmail.com',
            'gamil.com': 'gmail.com',
            'gmail.con': 'gmail.com',
            'hotmail.con': 'hotmail.com',
            'yahoo.con': 'yahoo.com',
            'outlook.con': 'outlook.com'
        }
    
    def _load_disposable_domains(self):
        """Load list of disposable email domains"""
        domains = [
            'tempmail.com', '10minutemail.com', 'guerrillamail.com',
            'mailinator.com', 'yopmail.com', 'trashmail.com',
            'throwawaymail.com', 'fakeinbox.com', 'tempmailaddress.com',
            'dispostable.com', 'mailmetrash.com', 'mailnesia.com',
            'spamgourmet.com', 'getairmail.com', 'maildrop.cc'
        ]
        
        # Try to load from file
        if os.path.exists("disposable_domains.txt"):
            with open("disposable_domains.txt", 'r') as f:
                domains.extend([line.strip() for line in f if line.strip()])
        
        return set(domains)
    
    def validate(self, email: str) -> Dict[str, Any]:
        """Advanced email validation with multiple checks"""
        result = {
            'valid': False,
            'email': email,
            'domain': None,
            'username': None,
            'is_disposable': False,
            'has_typo': False,
            'suggested_correction': None,
            'mx_records': [],
            'dns_valid': False,
            'format_valid': False
        }
        
        if not email or '@' not in email:
            return result
        
        # Basic format validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return result
        
        result['format_valid'] = True
        
        # Extract parts
        username, domain = email.split('@')
        result['username'] = username
        result['domain'] = domain.lower()
        
        # Check for typos
        corrected_domain = self.typo_domains.get(domain.lower())
        if corrected_domain:
            result['has_typo'] = True
            result['suggested_correction'] = f"{username}@{corrected_domain}"
        
        # Check disposable domains
        if any(disposable in domain.lower() for disposable in self.disposable_domains):
            result['is_disposable'] = True
            return result
        
        # Check DNS MX records
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            mx_records = [str(r.exchange) for r in answers]
            result['mx_records'] = mx_records
            result['dns_valid'] = len(mx_records) > 0
        except:
            result['dns_valid'] = False
        
        # Additional checks
        if len(username) > 64:
            return result
        
        if len(domain) > 255:
            return result
        
        result['valid'] = result['format_valid'] and result['dns_valid'] and not result['is_disposable']
        
        return result
    
    def extract_common_patterns(self, email: str) -> Dict[str, Any]:
        """Extract common patterns from email"""
        username, domain = email.split('@') if '@' in email else ('', '')
        
        return {
            'has_numbers': bool(re.search(r'\d', username)),
            'has_special': bool(re.search(r'[._%+-]', username)),
            'is_common_name': username.lower() in ['admin', 'contact', 'info', 'support', 'sales'],
            'length': len(username),
            'domain_type': self._classify_domain(domain)
        }
    
    def _classify_domain(self, domain: str) -> str:
        """Classify domain type"""
        domain = domain.lower()
        
        if 'gmail' in domain:
            return 'personal'
        elif 'yahoo' in domain:
            return 'personal'
        elif 'outlook' in domain or 'hotmail' in domain:
            return 'personal'
        elif 'edu' in domain:
            return 'educational'
        elif 'gov' in domain:
            return 'government'
        elif 'org' in domain:
            return 'organization'
        elif 'co.' in domain or 'com.' in domain:
            return 'commercial'
        else:
            return 'other'

# ========== ADVANCED PROXY MANAGER ==========
class AdvancedProxyManager:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.proxies = []
        self.working_proxies = []
        self.banned_proxies = []
        self.proxy_stats = {}
        self.user_agents = []
        self.ua = UserAgent()
        self.load_proxies()
        self.load_user_agents()
    
    def load_proxies(self):
        """Load and validate proxies"""
        sources = [
            self.config.PROXIES_FILE,
            "proxy_list.txt",
            "proxies/http.txt",
            "proxies/socks4.txt",
            "proxies/socks5.txt"
        ]
        
        all_proxies = set()
        
        for source in sources:
            if os.path.exists(source):
                try:
                    with open(source, 'r') as f:
                        proxies = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                        all_proxies.update(proxies)
                        self.logger.log('info', f"Loaded {len(proxies)} proxies from {source}")
                except Exception as e:
                    self.logger.log('error', f"Error loading {source}: {e}")
        
        # Add built-in proxies
        builtin_proxies = [
            "http://proxy-server:8080",
            "socks5://localhost:1080"
        ]
        all_proxies.update(builtin_proxies)
        
        self.proxies = list(all_proxies)
        
        if not self.proxies:
            self.logger.log('warning', "No proxies loaded, using direct connection")
        else:
            self.logger.log('info', f"Total proxies: {len(self.proxies)}")
            self.test_proxies_async()
    
    def load_user_agents(self):
        """Load user agents"""
        self.user_agents = [
            self.ua.random,
            self.ua.chrome,
            self.ua.firefox,
            self.ua.safari,
            self.ua.edge,
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
        ]
        
        # Load custom user agents
        if os.path.exists("user_agents.txt"):
            with open("user_agents.txt", 'r') as f:
                custom_agents = [line.strip() for line in f if line.strip()]
                self.user_agents.extend(custom_agents)
    
    async def test_proxy_async(self, proxy, session):
        """Test a single proxy asynchronously"""
        try:
            test_url = "http://httpbin.org/ip"
            
            async with session.get(test_url, proxy=proxy, timeout=10, ssl=False) as response:
                if response.status == 200:
                    data = await response.json()
                    self.working_proxies.append(proxy)
                    self.proxy_stats[proxy] = {
                        'last_used': datetime.now(),
                        'success_count': 0,
                        'fail_count': 0,
                        'avg_response_time': 0,
                        'country': None
                    }
                    return True
        except:
            self.banned_proxies.append(proxy)
        
        return False
    
    def test_proxies_async(self):
        """Test all proxies asynchronously"""
        async def main():
            async with aiohttp.ClientSession() as session:
                tasks = []
                for proxy in self.proxies[:50]:  # Test first 50 proxies
                    task = asyncio.create_task(self.test_proxy_async(proxy, session))
                    tasks.append(task)
                
                results = await asyncio.gather(*tasks)
                working_count = sum(results)
                self.logger.log('info', f"Working proxies: {working_count}/{len(tasks)}")
        
        try:
            asyncio.run(main())
        except:
            pass
    
    def get_random_proxy(self):
        """Get a random working proxy"""
        if not self.working_proxies:
            return None
        
        proxy = random.choice(self.working_proxies)
        
        # Update stats
        if proxy in self.proxy_stats:
            self.proxy_stats[proxy]['last_used'] = datetime.now()
            self.proxy_stats[proxy]['success_count'] += 1
        
        return proxy
    
    def get_random_user_agent(self):
        """Get random user agent"""
        return random.choice(self.user_agents)
    
    def get_proxy_stats(self):
        """Get proxy statistics"""
        return {
            'total': len(self.proxies),
            'working': len(self.working_proxies),
            'banned': len(self.banned_proxies),
            'stats': self.proxy_stats
        }

# ========== ENHANCED NETWORK ENGINE ==========
class EnhancedNetworkEngine:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.proxy_manager = AdvancedProxyManager(config, logger)
        self.sessions = {}
        self.request_count = 0
        self.circuit_breaker = {}
        self.domain_cooldowns = {}
    
    def create_session(self, use_proxy=True):
        """Create a new requests session"""
        session = requests.Session()
        
        # Headers
        headers = {
            'User-Agent': self.proxy_manager.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
        }
        
        session.headers.update(headers)
        
        # Cookies
        session.cookies.set('cookie_consent', 'true')
        
        # Proxy
        if use_proxy and self.proxy_manager.working_proxies:
            proxy = self.proxy_manager.get_random_proxy()
            if proxy:
                session.proxies = {
                    'http': proxy,
                    'https': proxy
                }
        
        # Tor proxy
        if self.config.USE_TOR_PROXY:
            session.proxies = {
                'http': self.config.TOR_PROXY,
                'https': self.config.TOR_PROXY
            }
        
        return session
    
    def get_session(self):
        """Get or create session for current thread"""
        thread_id = threading.get_ident()
        if thread_id not in self.sessions:
            self.sessions[thread_id] = self.create_session()
        
        # Rotate session every N requests
        if self.request_count % self.config.ROTATE_PROXY_EVERY == 0:
            self.sessions[thread_id] = self.create_session()
        
        return self.sessions[thread_id]
    
    def check_circuit_breaker(self, domain):
        """Check if domain is in circuit breaker state"""
        if domain in self.circuit_breaker:
            last_fail, fail_count = self.circuit_breaker[domain]
            if fail_count > 3 and (datetime.now() - last_fail).seconds < 300:
                return False
        return True
    
    def update_circuit_breaker(self, domain, success):
        """Update circuit breaker state"""
        if domain not in self.circuit_breaker:
            self.circuit_breaker[domain] = (datetime.now(), 0)
        
        last_fail, fail_count = self.circuit_breaker[domain]
        if success:
            self.circuit_breaker[domain] = (datetime.now(), 0)
        else:
            self.circuit_breaker[domain] = (datetime.now(), fail_count + 1)
    
    def smart_request(self, method, url, **kwargs):
        """Enhanced smart request with advanced features"""
        self.request_count += 1
        
        # Extract domain for circuit breaker
        domain = urlparse(url).netloc
        
        # Check circuit breaker
        if not self.check_circuit_breaker(domain):
            self.logger.log('warning', f"Circuit breaker active for {domain}")
            return None
        
        max_retries = kwargs.pop('max_retries', self.config.MAX_RETRIES)
        timeout = kwargs.pop('timeout', self.config.TIMEOUT)
        bypass_cache = kwargs.pop('bypass_cache', False)
        
        for attempt in range(max_retries + 1):
            try:
                session = self.get_session()
                
                # Random delay
                delay = random.uniform(0.1, 1.0)
                time.sleep(delay)
                
                # Make request
                response = session.request(
                    method, url,
                    timeout=timeout,
                    verify=False,
                    allow_redirects=True,
                    **kwargs
                )
                
                # Update circuit breaker
                self.update_circuit_breaker(domain, True)
                
                # Check status
                if response.status_code == 429:  # Rate limited
                    wait_time = random.uniform(10, 30)
                    self.logger.log('warning', f"Rate limited, waiting {wait_time:.1f}s")
                    time.sleep(wait_time)
                    continue
                
                elif response.status_code == 403:  # Forbidden
                    self.logger.log('warning', f"403 Forbidden for {url}")
                    # Rotate session
                    thread_id = threading.get_ident()
                    self.sessions[thread_id] = self.create_session()
                    continue
                
                elif response.status_code == 200:
                    return response
                
                else:
                    self.logger.log('debug', f"Status {response.status_code} for {url}")
                
            except requests.exceptions.Timeout:
                self.logger.log('warning', f"Timeout on attempt {attempt + 1}")
                if attempt == max_retries:
                    self.update_circuit_breaker(domain, False)
                    raise
            
            except requests.exceptions.ConnectionError:
                self.logger.log('warning', f"Connection error on attempt {attempt + 1}")
                # Rotate proxy
                thread_id = threading.get_ident()
                if thread_id in self.sessions:
                    del self.sessions[thread_id]
                
                if attempt == max_retries:
                    self.update_circuit_breaker(domain, False)
                    raise
            
            except Exception as e:
                self.logger.log('error', f"Request error: {e}")
                if attempt == max_retries:
                    self.update_circuit_breaker(domain, False)
                    raise
            
            # Exponential backoff
            time.sleep(2 ** attempt)
        
        return None

# ========== ENHANCED CACHE ENGINE ==========
class EnhancedCacheEngine:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.cache = {}
        self.stats = {'hits': 0, 'misses': 0, 'size': 0}
        self.cipher = Fernet(config.ENCRYPTION_KEY) if config.ENABLE_ENCRYPTION else None
        self.load_cache()
    
    def encrypt_data(self, data):
        """Encrypt cache data"""
        if not self.cipher or not self.config.ENABLE_ENCRYPTION:
            return data
        
        try:
            serialized = pickle.dumps(data)
            encrypted = self.cipher.encrypt(serialized)
            return encrypted
        except:
            return data
    
    def decrypt_data(self, data):
        """Decrypt cache data"""
        if not self.cipher or not self.config.ENABLE_ENCRYPTION:
            return data
        
        try:
            decrypted = self.cipher.decrypt(data)
            return pickle.loads(decrypted)
        except:
            return data
    
    def compress_data(self, data):
        """Compress data"""
        if not self.config.COMPRESS_CACHE:
            return data
        
        try:
            return zlib.compress(data)
        except:
            return data
    
    def decompress_data(self, data):
        """Decompress data"""
        if not self.config.COMPRESS_CACHE:
            return data
        
        try:
            return zlib.decompress(data)
        except:
            return data
    
    def load_cache(self):
        """Load cache from encrypted file"""
        try:
            if os.path.exists(self.config.CACHE_FILE):
                with open(self.config.CACHE_FILE, 'rb') as f:
                    data = f.read()
                
                if self.config.COMPRESS_CACHE:
                    data = self.decompress_data(data)
                
                data = self.decrypt_data(data)
                
                if isinstance(data, dict):
                    # Filter expired entries
                    current_time = time.time()
                    self.cache = {
                        k: v for k, v in data.items()
                        if current_time - v.get('timestamp', 0) < self.config.CACHE_EXPIRE_HOURS * 3600
                    }
                    
                    self.stats['size'] = len(self.cache)
                    self.logger.log('info', f"Cache loaded: {len(self.cache)} entries")
                else:
                    self.logger.log('warning', "Cache file corrupted")
        except Exception as e:
            self.logger.log('error', f"Cache load error: {e}")
            self.cache = {}
    
    def save_cache(self):
        """Save cache to encrypted file"""
        try:
            # Limit cache size
            if len(self.cache) > self.config.MAX_CACHE_SIZE:
                # Remove oldest 20%
                items = sorted(self.cache.items(), key=lambda x: x[1].get('timestamp', 0))
                keep_count = int(self.config.MAX_CACHE_SIZE * 0.8)
                self.cache = dict(items[-keep_count:])
            
            # Prepare data
            cache_data = self.cache.copy()
            
            # Encrypt
            if self.config.ENABLE_ENCRYPTION:
                cache_data = self.encrypt_data(cache_data)
            
            # Compress
            if self.config.COMPRESS_CACHE:
                cache_data = self.compress_data(cache_data)
            
            # Save
            with open(self.config.CACHE_FILE, 'wb') as f:
                f.write(cache_data)
            
            self.logger.log('debug', f"Cache saved: {len(self.cache)} entries")
            
        except Exception as e:
            self.logger.log('error', f"Cache save error: {e}")
    
    def get(self, key):
        """Get value from cache"""
        if key in self.cache:
            entry = self.cache[key]
            
            # Check expiry
            if time.time() - entry.get('timestamp', 0) < self.config.CACHE_EXPIRE_HOURS * 3600:
                self.stats['hits'] += 1
                entry['access_count'] = entry.get('access_count', 0) + 1
                entry['last_accessed'] = time.time()
                return entry['value']
        
        self.stats['misses'] += 1
        return None
    
    def set(self, key, value, ttl=None):
        """Set value in cache"""
        self.cache[key] = {
            'value': value,
            'timestamp': time.time(),
            'ttl': ttl or self.config.CACHE_EXPIRE_HOURS * 3600,
            'access_count': 0,
            'last_accessed': time.time()
        }
        
        # Auto-save every 100 entries
        if len(self.cache) % 100 == 0:
            self.save_cache()
    
    def get_stats(self):
        """Get cache statistics"""
        total = self.stats['hits'] + self.stats['misses']
        hit_rate = (self.stats['hits'] / total * 100) if total > 0 else 0
        
        # Calculate average age
        current_time = time.time()
        total_age = 0
        for entry in self.cache.values():
            total_age += current_time - entry.get('timestamp', current_time)
        
        avg_age = total_age / len(self.cache) if self.cache else 0
        
        return {
            'hits': self.stats['hits'],
            'misses': self.stats['misses'],
            'total': total,
            'hit_rate': hit_rate,
            'size': len(self.cache),
            'avg_age_hours': avg_age / 3600,
            'memory_mb': sys.getsizeof(self.cache) / (1024 * 1024)
        }
    
    def clear_expired(self):
        """Clear expired cache entries"""
        current_time = time.time()
        expired_count = 0
        
        keys_to_delete = []
        for key, entry in self.cache.items():
            if current_time - entry.get('timestamp', 0) > entry.get('ttl', self.config.CACHE_EXPIRE_HOURS * 3600):
                keys_to_delete.append(key)
                expired_count += 1
        
        for key in keys_to_delete:
            del self.cache[key]
        
        if expired_count > 0:
            self.logger.log('info', f"Cleared {expired_count} expired cache entries")
            self.save_cache()
    
    def export_cache(self, filename):
        """Export cache to file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.cache, f, indent=2, default=str)
            self.logger.log('info', f"Cache exported to {filename}")
        except Exception as e:
            self.logger.log('error', f"Export error: {e}")

# ========== ENHANCED DATABASE ENGINE ==========
class EnhancedDatabaseEngine:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.conn = None
        self.init_database()
        self.create_backup()
    
    def init_database(self):
        """Initialize enhanced SQLite database"""
        try:
            self.conn = sqlite3.connect(self.config.DB_FILE, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            cursor = self.conn.cursor()
            
            # Enable WAL mode for better concurrency
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA synchronous=NORMAL")
            cursor.execute("PRAGMA cache_size=-2000")  # 2MB cache
            
            # Create emails table with more fields
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS emails (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    domain TEXT NOT NULL,
                    username TEXT,
                    is_valid BOOLEAN DEFAULT 1,
                    is_disposable BOOLEAN DEFAULT 0,
                    has_typo BOOLEAN DEFAULT 0,
                    suggested_correction TEXT,
                    mx_valid BOOLEAN DEFAULT 0,
                    dns_valid BOOLEAN DEFAULT 0,
                    breach_count INTEGER DEFAULT 0,
                    password_strength INTEGER DEFAULT 0,
                    reputation_score FLOAT DEFAULT 0.0,
                    check_count INTEGER DEFAULT 0,
                    last_checked TIMESTAMP,
                    first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_premium BOOLEAN DEFAULT 0,
                    tags TEXT,
                    notes TEXT,
                    INDEX idx_email (email),
                    INDEX idx_domain (domain),
                    INDEX idx_last_checked (last_checked)
                )
            ''')
            
            # Create results table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email_id INTEGER NOT NULL,
                    service_name TEXT NOT NULL,
                    service_category TEXT,
                    is_found BOOLEAN NOT NULL,
                    confidence FLOAT DEFAULT 1.0,
                    check_time FLOAT,
                    response_code INTEGER,
                    raw_response TEXT,
                    metadata TEXT,
                    check_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (email_id) REFERENCES emails (id) ON DELETE CASCADE,
                    INDEX idx_service (service_name),
                    INDEX idx_found (is_found),
                    INDEX idx_email_service (email_id, service_name)
                )
            ''')
            
            # Create services table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    category TEXT,
                    check_method TEXT,
                    api_endpoint TEXT,
                    success_pattern TEXT,
                    is_active BOOLEAN DEFAULT 1,
                    priority INTEGER DEFAULT 5,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    success_rate FLOAT DEFAULT 0.0,
                    avg_response_time FLOAT DEFAULT 0.0,
                    daily_quota INTEGER DEFAULT 1000
                )
            ''')
            
            # Create breaches table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS breaches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email_id INTEGER NOT NULL,
                    breach_name TEXT NOT NULL,
                    breach_date TEXT,
                    compromised_data TEXT,
                    description TEXT,
                    severity INTEGER DEFAULT 1,
                    reported_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (email_id) REFERENCES emails (id) ON DELETE CASCADE
                )
            ''')
            
            # Create statistics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS statistics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE UNIQUE NOT NULL,
                    total_checks INTEGER DEFAULT 0,
                    successful_checks INTEGER DEFAULT 0,
                    failed_checks INTEGER DEFAULT 0,
                    unique_emails INTEGER DEFAULT 0,
                    new_emails INTEGER DEFAULT 0,
                    avg_check_time FLOAT DEFAULT 0.0,
                    cache_hit_rate FLOAT DEFAULT 0.0,
                    proxy_usage INTEGER DEFAULT 0,
                    peak_concurrent INTEGER DEFAULT 0
                )
            ''')
            
            # Create tags table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tags (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email_id INTEGER NOT NULL,
                    tag TEXT NOT NULL,
                    color TEXT DEFAULT '#FFFFFF',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (email_id) REFERENCES emails (id) ON DELETE CASCADE,
                    UNIQUE(email_id, tag)
                )
            ''')
            
            self.conn.commit()
            self.logger.log('info', "Database initialized successfully")
            
            # Insert default services
            self.insert_default_services()
            
        except Exception as e:
            self.logger.log('error', f"Database error: {e}")
            raise
    
    def insert_default_services(self):
        """Insert default services"""
        default_services = [
            ('Facebook', 'Social Media', 'api_check', 'https://facebook.com', 'SUCCESS', 1, 95.5),
            ('Instagram', 'Social Media', 'api_check', 'https://instagram.com', 'SUCCESS', 1, 92.3),
            ('Twitter', 'Social Media', 'api_check', 'https://twitter.com', 'SUCCESS', 1, 90.1),
            ('Google', 'Email', 'mx_check', 'https://google.com', 'SUCCESS', 1, 98.0),
            ('Microsoft', 'Email', 'mx_check', 'https://microsoft.com', 'SUCCESS', 2, 96.5),
        ]
        
        cursor = self.conn.cursor()
        for service in default_services:
            cursor.execute('''
                INSERT OR IGNORE INTO services (name, category, check_method, api_endpoint, success_pattern, priority, success_rate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', service)
        
        self.conn.commit()
    
    def create_backup(self):
        """Create database backup"""
        if not os.path.exists(self.config.BACKUP_DIR):
            os.makedirs(self.config.BACKUP_DIR)
        
        backup_file = os.path.join(
            self.config.BACKUP_DIR,
            f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        )
        
        try:
            # Create backup connection
            backup_conn = sqlite3.connect(backup_file)
            self.conn.backup(backup_conn)
            backup_conn.close()
            
            # Compress backup
            with open(backup_file, 'rb') as f:
                data = f.read()
            
            compressed = zlib.compress(data)
            with open(backup_file + '.gz', 'wb') as f:
                f.write(compressed)
            
            os.remove(backup_file)
            self.logger.log('info', f"Database backup created: {backup_file}.gz")
            
        except Exception as e:
            self.logger.log('error', f"Backup error: {e}")
    
    def save_email_result(self, email, validation_result, service_results, check_time):
        """Save email check results with enhanced details"""
        try:
            cursor = self.conn.cursor()
            
            # Save or update email
            cursor.execute('''
                INSERT OR REPLACE INTO emails (
                    email, domain, username, is_valid, is_disposable, has_typo,
                    suggested_correction, mx_valid, dns_valid, check_count,
                    last_checked, last_seen
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 
                    COALESCE((SELECT check_count FROM emails WHERE email = ?), 0) + 1,
                    CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
                )
            ''', (
                email,
                validation_result.get('domain'),
                validation_result.get('username'),
                validation_result.get('valid'),
                validation_result.get('is_disposable'),
                validation_result.get('has_typo'),
                validation_result.get('suggested_correction'),
                validation_result.get('dns_valid'),
                validation_result.get('dns_valid'),
                email
            ))
            
            email_id = cursor.lastrowid or cursor.execute(
                "SELECT id FROM emails WHERE email = ?", (email,)
            ).fetchone()[0]
            
            # Save service results
            for service_name, result in service_results.items():
                if isinstance(result, dict):
                    is_found = result.get('found', False)
                    confidence = result.get('confidence', 1.0)
                    metadata = json.dumps(result.get('metadata', {}))
                else:
                    is_found = result
                    confidence = 1.0
                    metadata = '{}'
                
                cursor.execute('''
                    INSERT INTO results (email_id, service_name, is_found, confidence, check_time, metadata)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (email_id, service_name, is_found, confidence, check_time, metadata))
            
            # Update service statistics
            for service_name in service_results.keys():
                cursor.execute('''
                    UPDATE services 
                    SET success_rate = (
                        SELECT (COUNT(CASE WHEN is_found = 1 THEN 1 END) * 100.0 / COUNT(*)) 
                        FROM results WHERE service_name = ?
                    ),
                    avg_response_time = (
                        SELECT AVG(check_time) FROM results WHERE service_name = ? AND check_time IS NOT NULL
                    ),
                    last_updated = CURRENT_TIMESTAMP
                    WHERE name = ?
                ''', (service_name, service_name, service_name))
            
            self.conn.commit()
            return True
            
        except Exception as e:
            self.logger.log('error', f"Database save error: {e}")
            self.conn.rollback()
            return False
    
    def get_email_stats(self, email):
        """Get detailed statistics for an email"""
        try:
            cursor = self.conn.cursor()
            
            cursor.execute('''
                SELECT 
                    e.check_count,
                    e.last_checked,
                    e.first_seen,
                    e.reputation_score,
                    e.breach_count,
                    COUNT(r.id) as total_checks,
                    SUM(CASE WHEN r.is_found = 1 THEN 1 ELSE 0 END) as found_count
                FROM emails e
                LEFT JOIN results r ON e.id = r.email_id
                WHERE e.email = ?
                GROUP BY e.id
            ''', (email,))
            
            result = cursor.fetchone()
            if result:
                return dict(result)
            
        except Exception as e:
            self.logger.log('error', f"Stats error: {e}")
        
        return {}
    
    def get_dashboard_stats(self):
        """Get dashboard statistics"""
        try:
            cursor = self.conn.cursor()
            
            stats = {}
            
            # Basic counts
            cursor.execute("SELECT COUNT(*) FROM emails")
            stats['total_emails'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(DISTINCT email) FROM emails WHERE last_checked >= datetime('now', '-1 day')")
            stats['checked_today'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM results WHERE is_found = 1")
            stats['total_found'] = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(DISTINCT service_name) FROM results")
            stats['total_services'] = cursor.fetchone()[0]
            
            # Top domains
            cursor.execute('''
                SELECT domain, COUNT(*) as count 
                FROM emails 
                GROUP BY domain 
                ORDER BY count DESC 
                LIMIT 5
            ''')
            stats['top_domains'] = [dict(row) for row in cursor.fetchall()]
            
            # Service success rates
            cursor.execute('''
                SELECT 
                    service_name,
                    COUNT(*) as total,
                    SUM(CASE WHEN is_found = 1 THEN 1 ELSE 0 END) as found,
                    ROUND((SUM(CASE WHEN is_found = 1 THEN 1.0 ELSE 0 END) / COUNT(*) * 100), 2) as success_rate
                FROM results 
                GROUP BY service_name 
                ORDER BY success_rate DESC 
                LIMIT 10
            ''')
            stats['top_services'] = [dict(row) for row in cursor.fetchall()]
            
            return stats
            
        except Exception as e:
            self.logger.log('error', f"Dashboard stats error: {e}")
            return {}
    
    def export_to_csv(self, filename, query=None):
        """Export results to CSV with advanced options"""
        try:
            cursor = self.conn.cursor()
            
            if query:
                cursor.execute(query)
            else:
                cursor.execute('''
                    SELECT 
                        e.email,
                        e.domain,
                        e.is_valid,
                        e.is_disposable,
                        e.breach_count,
                        e.reputation_score,
                        e.last_checked,
                        GROUP_CONCAT(r.service_name || ':' || r.is_found) as results
                    FROM emails e
                    LEFT JOIN results r ON e.id = r.email_id
                    GROUP BY e.email
                    ORDER BY e.last_checked DESC
                ''')
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow([desc[0] for desc in cursor.description])
                
                # Write data
                writer.writerows(cursor.fetchall())
            
            self.logger.log('info', f"Exported to {filename}")
            return True
            
        except Exception as e:
            self.logger.log('error', f"Export error: {e}")
            return False
    
    def search_emails(self, query, limit=100):
        """Search emails with advanced filters"""
        try:
            cursor = self.conn.cursor()
            
            # Build search query
            sql = '''
                SELECT DISTINCT e.*,
                    (SELECT COUNT(*) FROM results r WHERE r.email_id = e.id AND r.is_found = 1) as found_count
                FROM emails e
                LEFT JOIN results r ON e.id = r.email_id
                WHERE 1=1
            '''
            params = []
            
            if query.get('email'):
                sql += " AND e.email LIKE ?"
                params.append(f"%{query['email']}%")
            
            if query.get('domain'):
                sql += " AND e.domain = ?"
                params.append(query['domain'])
            
            if query.get('is_valid') is not None:
                sql += " AND e.is_valid = ?"
                params.append(query['is_valid'])
            
            if query.get('has_breaches') is not None:
                if query['has_breaches']:
                    sql += " AND e.breach_count > 0"
                else:
                    sql += " AND e.breach_count = 0"
            
            if query.get('service'):
                sql += " AND r.service_name = ? AND r.is_found = 1"
                params.append(query['service'])
            
            sql += " ORDER BY e.last_checked DESC LIMIT ?"
            params.append(limit)
            
            cursor.execute(sql, params)
            return [dict(row) for row in cursor.fetchall()]
            
        except Exception as e:
            self.logger.log('error', f"Search error: {e}")
            return []

# ========== ADVANCED SERVICE CHECKERS ==========
class AdvancedServiceCheckers:
    def __init__(self, network_engine, cache_engine, logger):
        self.network = network_engine
        self.cache = cache_engine
        self.logger = logger
        
        # Enhanced service configurations
        self.services = {
            # Social Media (Priority 1)
            "Facebook": {
                "emoji": "👤", "color": Fore.BLUE, "priority": 1, "category": "Social Media",
                "check_method": self.check_facebook,
                "endpoints": ["https://www.facebook.com/login/identify"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Instagram": {
                "emoji": "📷", "color": Fore.MAGENTA, "priority": 1, "category": "Social Media",
                "check_method": self.check_instagram,
                "endpoints": ["https://www.instagram.com"],
                "api_key_required": False,
                "rate_limit": 200
            },
            "Twitter/X": {
                "emoji": "🐦", "color": Fore.CYAN, "priority": 1, "category": "Social Media",
                "check_method": self.check_twitter,
                "endpoints": ["https://twitter.com"],
                "api_key_required": False,
                "rate_limit": 150
            },
            "TikTok": {
                "emoji": "📱", "color": Fore.BLACK, "priority": 1, "category": "Social Media",
                "check_method": self.check_tiktok,
                "endpoints": ["https://www.tiktok.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "LinkedIn": {
                "emoji": "💼", "color": Fore.BLUE, "priority": 1, "category": "Professional",
                "check_method": self.check_linkedin,
                "endpoints": ["https://www.linkedin.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Snapchat": {
                "emoji": "👻", "color": Fore.YELLOW, "priority": 1, "category": "Social Media",
                "check_method": self.check_snapchat,
                "endpoints": ["https://accounts.snapchat.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            
            # Email Services (Priority 2)
            "Google/Gmail": {
                "emoji": "🔍", "color": Fore.RED, "priority": 2, "category": "Email",
                "check_method": self.check_google,
                "endpoints": ["https://accounts.google.com"],
                "api_key_required": False,
                "rate_limit": 1000
            },
            "Microsoft/Outlook": {
                "emoji": "🪟", "color": Fore.BLUE, "priority": 2, "category": "Email",
                "check_method": self.check_microsoft,
                "endpoints": ["https://login.live.com"],
                "api_key_required": False,
                "rate_limit": 500
            },
            "Yahoo Mail": {
                "emoji": "📬", "color": Fore.MAGENTA, "priority": 2, "category": "Email",
                "check_method": self.check_yahoo,
                "endpoints": ["https://login.yahoo.com"],
                "api_key_required": False,
                "rate_limit": 300
            },
            "ProtonMail": {
                "emoji": "🔒", "color": Fore.BLUE, "priority": 2, "category": "Email",
                "check_method": self.check_protonmail,
                "endpoints": ["https://account.protonmail.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            
            # Entertainment (Priority 3)
            "Netflix": {
                "emoji": "🎬", "color": Fore.RED, "priority": 3, "category": "Entertainment",
                "check_method": self.check_netflix,
                "endpoints": ["https://www.netflix.com"],
                "api_key_required": False,
                "rate_limit": 200
            },
            "Spotify": {
                "emoji": "🎵", "color": Fore.GREEN, "priority": 3, "category": "Entertainment",
                "check_method": self.check_spotify,
                "endpoints": ["https://www.spotify.com"],
                "api_key_required": False,
                "rate_limit": 200
            },
            "Twitch": {
                "emoji": "🟣", "color": Fore.MAGENTA, "priority": 3, "category": "Entertainment",
                "check_method": self.check_twitch,
                "endpoints": ["https://www.twitch.tv"],
                "api_key_required": False,
                "rate_limit": 150
            },
            "Steam": {
                "emoji": "🎮", "color": Fore.WHITE, "priority": 3, "category": "Gaming",
                "check_method": self.check_steam,
                "endpoints": ["https://store.steampowered.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Discord": {
                "emoji": "🎮", "color": Fore.CYAN, "priority": 3, "category": "Communication",
                "check_method": self.check_discord,
                "endpoints": ["https://discord.com"],
                "api_key_required": False,
                "rate_limit": 150
            },
            
            # E-commerce & Finance (Priority 4)
            "Amazon": {
                "emoji": "📦", "color": Fore.YELLOW, "priority": 4, "category": "E-commerce",
                "check_method": self.check_amazon,
                "endpoints": ["https://www.amazon.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "eBay": {
                "emoji": "🛒", "color": Fore.YELLOW, "priority": 4, "category": "E-commerce",
                "check_method": self.check_ebay,
                "endpoints": ["https://www.ebay.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "PayPal": {
                "emoji": "💰", "color": Fore.BLUE, "priority": 4, "category": "Finance",
                "check_method": self.check_paypal,
                "endpoints": ["https://www.paypal.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Shopify": {
                "emoji": "🛍️", "color": Fore.GREEN, "priority": 4, "category": "E-commerce",
                "check_method": self.check_shopify,
                "endpoints": ["https://accounts.shopify.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            
            # Technology (Priority 5)
            "GitHub": {
                "emoji": "💻", "color": Fore.WHITE, "priority": 5, "category": "Technology",
                "check_method": self.check_github,
                "endpoints": ["https://github.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "GitLab": {
                "emoji": "🦊", "color": Fore.RED, "priority": 5, "category": "Technology",
                "check_method": self.check_gitlab,
                "endpoints": ["https://gitlab.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Dropbox": {
                "emoji": "📁", "color": Fore.BLUE, "priority": 5, "category": "Cloud",
                "check_method": self.check_dropbox,
                "endpoints": ["https://www.dropbox.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Adobe": {
                "emoji": "🎨", "color": Fore.RED, "priority": 5, "category": "Creative",
                "check_method": self.check_adobe,
                "endpoints": ["https://account.adobe.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            
            # Other Services (Priority 6)
            "Reddit": {
                "emoji": "👽", "color": Fore.RED, "priority": 6, "category": "Social Media",
                "check_method": self.check_reddit,
                "endpoints": ["https://www.reddit.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Telegram": {
                "emoji": "📨", "color": Fore.CYAN, "priority": 6, "category": "Communication",
                "check_method": self.check_telegram,
                "endpoints": ["https://telegram.org"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Pinterest": {
                "emoji": "📌", "color": Fore.RED, "priority": 6, "category": "Social Media",
                "check_method": self.check_pinterest,
                "endpoints": ["https://www.pinterest.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Quora": {
                "emoji": "❓", "color": Fore.RED, "priority": 6, "category": "Q&A",
                "check_method": self.check_quora,
                "endpoints": ["https://www.quora.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Tumblr": {
                "emoji": "📝", "color": Fore.BLUE, "priority": 6, "category": "Blogging",
                "check_method": self.check_tumblr,
                "endpoints": ["https://www.tumblr.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Flickr": {
                "emoji": "📸", "color": Fore.MAGENTA, "priority": 6, "category": "Photography",
                "check_method": self.check_flickr,
                "endpoints": ["https://www.flickr.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "WordPress": {
                "emoji": "✍️", "color": Fore.BLUE, "priority": 6, "category": "Blogging",
                "check_method": self.check_wordpress,
                "endpoints": ["https://wordpress.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "VK": {
                "emoji": "🇷🇺", "color": Fore.BLUE, "priority": 6, "category": "Social Media",
                "check_method": self.check_vk,
                "endpoints": ["https://vk.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Weibo": {
                "emoji": "🇨🇳", "color": Fore.RED, "priority": 6, "category": "Social Media",
                "check_method": self.check_weibo,
                "endpoints": ["https://weibo.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            "Apple/iCloud": {
                "emoji": "🍎", "color": Fore.WHITE, "priority": 6, "category": "Email",
                "check_method": self.check_apple,
                "endpoints": ["https://appleid.apple.com"],
                "api_key_required": False,
                "rate_limit": 100
            },
            
            # Specialized Services (Priority 7)
            "HaveIBeenPwned": {
                "emoji": "⚠️", "color": Fore.RED, "priority": 7, "category": "Security",
                "check_method": self.check_hibp,
                "endpoints": ["https://haveibeenpwned.com"],
                "api_key_required": True,
                "rate_limit": 10
            },
            "EmailRep": {
                "emoji": "🛡️", "color": Fore.GREEN, "priority": 7, "category": "Reputation",
                "check_method": self.check_emailrep,
                "endpoints": ["https://emailrep.io"],
                "api_key_required": True,
                "rate_limit": 100
            },
            "Hunter.io": {
                "emoji": "🎯", "color": Fore.BLUE, "priority": 7, "category": "Verification",
                "check_method": self.check_hunter,
                "endpoints": ["https://hunter.io"],
                "api_key_required": True,
                "rate_limit": 50
            },
            "DeHashed": {
                "emoji": "🔓", "color": Fore.RED, "priority": 7, "category": "Security",
                "check_method": self.check_dehashed,
                "endpoints": ["https://dehashed.com"],
                "api_key_required": True,
                "rate_limit": 20
            }
        }
        
        # Initialize API clients
        self.hibp_client = None
        self.emailrep_client = None
        self.hunter_client = None
        self.dehashed_client = None
        
        self.init_api_clients()
    
    def init_api_clients(self):
        """Initialize API clients"""
        # This is a placeholder for actual API client initialization
        # In production, you would initialize actual API clients here
        pass
    
    # ========== ENHANCED CHECK METHODS ==========
    
    def check_facebook(self, email):
        """Enhanced Facebook check with multiple methods"""
        cache_key = f"fb_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9, 'method': 'cache'}
        
        methods = [
            self._check_facebook_password_reset,
            self._check_facebook_mobile_api,
            self._check_facebook_graphql
        ]
        
        results = []
        for method in methods:
            try:
                result = method(email)
                if result['found']:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.95, 'method': method.__name__}
                results.append(result)
            except Exception as e:
                self.logger.log('debug', f"Facebook {method.__name__} failed: {e}")
        
        # If all methods failed, check cache
        if any(r['found'] for r in results if 'found' in r):
            self.cache.set(cache_key, True)
            return {'found': True, 'confidence': 0.8, 'method': 'fallback'}
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7, 'method': 'composite'}
    
    def _check_facebook_password_reset(self, email):
        """Check via password reset flow"""
        try:
            session = self.network.get_session()
            response = session.get(
                "https://www.facebook.com/login/identify",
                timeout=self.network.config.TIMEOUT
            )
            
            # Extract anti-CSRF tokens
            lsd_match = re.search(r'name="lsd" value="([^"]+)"', response.text)
            jazoest_match = re.search(r'name="jazoest" value="([^"]+)"', response.text)
            
            if lsd_match and jazoest_match:
                data = {
                    'lsd': lsd_match.group(1),
                    'jazoest': jazoest_match.group(1),
                    'email': email,
                    'did_submit': 'Search'
                }
                
                response2 = session.post(
                    "https://www.facebook.com/login/identify",
                    data=data,
                    timeout=self.network.config.TIMEOUT
                )
                
                text = response2.text.lower()
                indicators = ['send code', 'reset password', 'confirm your identity']
                
                if any(indicator in text for indicator in indicators):
                    return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"Facebook password reset check failed: {e}")
        
        return {'found': False, 'confidence': 0.6}
    
    def _check_facebook_mobile_api(self, email):
        """Check via mobile API"""
        try:
            response = self.network.smart_request(
                'GET',
                'https://mbasic.facebook.com/login/identify',
                params={'email': email},
                timeout=self.network.config.TIMEOUT
            )
            
            if response and 'find your account' in response.text.lower():
                return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"Facebook mobile API check failed: {e}")
        
        return {'found': False, 'confidence': 0.6}
    
    def _check_facebook_graphql(self, email):
        """Check via GraphQL endpoint (if available)"""
        # This is a placeholder for GraphQL-based check
        return {'found': False, 'confidence': 0.5}
    
    def check_instagram(self, email):
        """Enhanced Instagram check"""
        cache_key = f"ig_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            session = self.network.get_session()
            
            # Get CSRF token
            response = session.get(
                "https://www.instagram.com/accounts/password/reset/",
                timeout=self.network.config.TIMEOUT
            )
            
            csrf_match = re.search(r'"csrf_token":"([^"]+)"', response.text)
            if not csrf_match:
                self.cache.set(cache_key, False)
                return {'found': False, 'confidence': 0.6}
            
            csrf_token = csrf_match.group(1)
            
            headers = {
                'X-CSRFToken': csrf_token,
                'X-Instagram-AJAX': '100',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/password/reset/',
            }
            
            response2 = session.post(
                "https://www.instagram.com/accounts/account_recovery_send_ajax/",
                data={'email_or_username': email},
                headers=headers,
                timeout=self.network.config.TIMEOUT
            )
            
            if response2 and response2.status_code == 200:
                try:
                    data = response2.json()
                    if data.get('status') == 'ok' or 'user' in str(data).lower():
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.95}
                except:
                    if 'email_sent' in response2.text.lower():
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"Instagram check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_twitter(self, email):
        """Enhanced Twitter/X check"""
        cache_key = f"tw_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            session = self.network.get_session()
            
            # Try password reset page
            response = session.get(
                "https://twitter.com/account/begin_password_reset",
                timeout=self.network.config.TIMEOUT
            )
            
            authenticity_token_match = re.search(
                r'name="authenticity_token" value="([^"]+)"',
                response.text
            )
            
            if authenticity_token_match:
                token = authenticity_token_match.group(1)
                
                data = {
                    'authenticity_token': token,
                    'account_identifier': email
                }
                
                response2 = session.post(
                    "https://twitter.com/account/begin_password_reset",
                    data=data,
                    timeout=self.network.config.TIMEOUT
                )
                
                text = response2.text.lower()
                
                if any(phrase in text for phrase in [
                    'email has been sent',
                    'reset your password',
                    'password reset email'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.95}
                
                elif any(phrase in text for phrase in [
                    'no account found',
                    'could not find',
                    'not associated'
                ]):
                    self.cache.set(cache_key, False)
                    return {'found': False, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"Twitter check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.6}
    
    def check_tiktok(self, email):
        """Enhanced TikTok check"""
        cache_key = f"tt_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1'
            }
            
            response = self.network.smart_request(
                'POST',
                'https://www.tiktok.com/api/user/check_email/',
                json={'email': email},
                headers=headers
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('data', {}).get('exist', False):
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.95}
                except:
                    pass
            
            # Alternative method
            response2 = self.network.smart_request(
                'GET',
                f'https://www.tiktok.com/@{email}',
                headers={'User-Agent': headers['User-Agent']}
            )
            
            if response2 and response2.status_code != 404:
                self.cache.set(cache_key, True)
                return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"TikTok check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_google(self, email):
        """Enhanced Google/Gmail check"""
        # Gmail always has account
        if email.lower().endswith('@gmail.com'):
            return {'found': True, 'confidence': 1.0, 'metadata': {'is_gmail': True}}
        
        cache_key = f"google_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            username = email.split('@')[0]
            
            # Check Google signup API
            response = self.network.smart_request(
                'GET',
                'https://accounts.google.com/_/signup/webusernameavailability',
                params={
                    'username': username,
                    'hl': 'en'
                }
            )
            
            if response and response.status_code == 200:
                if 'NAME_NOT_AVAILABLE' in response.text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.95}
                elif 'NAME_AVAILABLE' in response.text:
                    self.cache.set(cache_key, False)
                    return {'found': False, 'confidence': 0.9}
            
            # Check MX records
            try:
                domain = email.split('@')[1]
                answers = dns.resolver.resolve(domain, 'MX')
                if len(answers) > 0:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8, 'metadata': {'mx_found': True}}
            except:
                pass
            
            # Check Google Workspace
            try:
                response2 = self.network.smart_request(
                    'POST',
                    'https://accounts.google.com/InputValidator?resource=SignUp',
                    json={'email': email}
                )
                
                if response2 and response2.status_code == 200:
                    data = response2.json()
                    if not data.get('valid', True):
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.85}
            except:
                pass
        
        except Exception as e:
            self.logger.log('debug', f"Google check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_microsoft(self, email):
        """Enhanced Microsoft check"""
        cache_key = f"ms_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://login.live.com/GetCredentialType.srf',
                json={'Username': email}
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    if_exists = data.get('IfExistsResult', -1)
                    
                    # 0 = Account exists
                    # 1 = Account doesn't exist
                    # 5 = Account exists but needs additional proof
                    
                    if if_exists in [0, 5]:
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.95}
                    elif if_exists == 1:
                        self.cache.set(cache_key, False)
                        return {'found': False, 'confidence': 0.9}
                except:
                    pass
            
            # Alternative method
            response2 = self.network.smart_request(
                'GET',
                f'https://login.live.com/login.srf?email={email}',
                allow_redirects=False
            )
            
            if response2 and response2.status_code in [200, 302]:
                self.cache.set(cache_key, True)
                return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Microsoft check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_yahoo(self, email):
        """Enhanced Yahoo check"""
        # Yahoo Mail always has account
        if email.lower().endswith('@yahoo.com'):
            return {'found': True, 'confidence': 1.0, 'metadata': {'is_yahoo': True}}
        
        cache_key = f"yh_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://login.yahoo.com/account/create',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'account with this email',
                    'already exists',
                    'taken'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
                
                elif any(phrase in text for phrase in [
                    'available',
                    'not found'
                ]):
                    self.cache.set(cache_key, False)
                    return {'found': False, 'confidence': 0.8}
            
            # Check MX records
            try:
                domain = email.split('@')[1]
                if 'yahoo' in domain.lower():
                    answers = dns.resolver.resolve(domain, 'MX')
                    if len(answers) > 0:
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.85}
            except:
                pass
        
        except Exception as e:
            self.logger.log('debug', f"Yahoo check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_protonmail(self, email):
        """Check ProtonMail account"""
        cache_key = f"pm_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            # ProtonMail has strict rate limiting, so we use a simple check
            if email.lower().endswith('@protonmail.com') or email.lower().endswith('@proton.me'):
                self.cache.set(cache_key, True)
                return {'found': True, 'confidence': 0.8}
            
            response = self.network.smart_request(
                'POST',
                'https://account.proton.me/api/auth/v4/sessions',
                json={'Username': email}
            )
            
            if response:
                if response.status_code == 400:
                    # 400 might mean account exists but password is wrong
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.7}
                elif response.status_code == 404:
                    self.cache.set(cache_key, False)
                    return {'found': False, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"ProtonMail check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.6}
    
    def check_netflix(self, email):
        """Enhanced Netflix check"""
        cache_key = f"nf_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.netflix.com/login',
                data={'userLoginId': email},
                allow_redirects=False
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'password',
                    'sign in',
                    'incorrect password'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
                
                elif 'create account' in text:
                    self.cache.set(cache_key, False)
                    return {'found': False, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Netflix check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    # ========== ADDITIONAL SERVICE METHODS ==========
    
    def check_linkedin(self, email):
        """Enhanced LinkedIn check"""
        cache_key = f"li_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.linkedin.com/uas/request-password-reset',
                data={'userName': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'reset password',
                    'email sent',
                    'account found'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"LinkedIn check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_github(self, email):
        """Enhanced GitHub check"""
        cache_key = f"gh_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://github.com/password_reset',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'check your email',
                    'password reset email',
                    'sent you an email'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"GitHub check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_gitlab(self, email):
        """Check GitLab account"""
        cache_key = f"gl_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://gitlab.com/users/password',
                data={'user[email]': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'email sent' in text or 'reset instructions' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"GitLab check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_dropbox(self, email):
        """Check Dropbox account"""
        cache_key = f"db_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.dropbox.com/forgot',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'reset link' in text or 'email sent' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"Dropbox check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_adobe(self, email):
        """Check Adobe account"""
        cache_key = f"ad_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://account.adobe.com/forgot-password',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'reset link' in text or 'email sent' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"Adobe check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_spotify(self, email):
        """Enhanced Spotify check"""
        cache_key = f"sp_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.spotify.com/api/signup/validate',
                json={'email': email}
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    status = data.get('status')
                    
                    # 20 = Email already registered
                    # 0 = Email available
                    
                    if status == 20:
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.95}
                    elif status == 0:
                        self.cache.set(cache_key, False)
                        return {'found': False, 'confidence': 0.9}
                except:
                    pass
        
        except Exception as e:
            self.logger.log('debug', f"Spotify check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_snapchat(self, email):
        """Enhanced Snapchat check"""
        cache_key = f"sc_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://accounts.snapchat.com/accounts/get_username_suggestions',
                json={'email': email}
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('has_used_email', False) or data.get('error_message', ''):
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.85}
                except:
                    if 'taken' in response.text.lower():
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Snapchat check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_amazon(self, email):
        """Enhanced Amazon check"""
        cache_key = f"amz_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.amazon.com/ap/signin',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'password',
                    'sign in',
                    'enter password'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"Amazon check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_ebay(self, email):
        """Enhanced eBay check"""
        cache_key = f"eb_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://signin.ebay.com/ws/eBayISAPI.dll',
                data={'userid': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'enter your password' in text or 'sign in' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"eBay check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_paypal(self, email):
        """Enhanced PayPal check"""
        cache_key = f"pp_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.paypal.com/authflow/password-recovery/',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'recovery',
                    'reset',
                    'email sent'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"PayPal check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_shopify(self, email):
        """Check Shopify account"""
        cache_key = f"sh_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://accounts.shopify.com/lookup',
                json={'email': email}
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('exists', False):
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.9}
                except:
                    pass
        
        except Exception as e:
            self.logger.log('debug', f"Shopify check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_discord(self, email):
        """Enhanced Discord check"""
        cache_key = f"dc_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            random_username = f'checker{random.randint(10000, 99999)}'
            
            response = self.network.smart_request(
                'POST',
                'https://discord.com/api/v9/auth/register',
                json={
                    'email': email,
                    'username': random_username,
                    'password': 'TestPass123!@#',
                    'date_of_birth': '1990-01-01'
                }
            )
            
            if response and response.status_code == 400:
                if 'EMAIL_ALREADY_REGISTERED' in response.text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.95}
        
        except Exception as e:
            self.logger.log('debug', f"Discord check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_twitch(self, email):
        """Enhanced Twitch check"""
        cache_key = f"twitch_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.twitch.tv/',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'password' in text or 'sign in' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Twitch check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_steam(self, email):
        """Enhanced Steam check"""
        cache_key = f"st_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://store.steampowered.com/join/checkavail/',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    if not data.get('bAvailable', True):
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.9}
                except:
                    pass
        
        except Exception as e:
            self.logger.log('debug', f"Steam check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_reddit(self, email):
        """Enhanced Reddit check"""
        cache_key = f"rd_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.reddit.com/account/register',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if any(phrase in text for phrase in [
                    'email already exists',
                    'already registered',
                    'taken'
                ]):
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.9}
        
        except Exception as e:
            self.logger.log('debug', f"Reddit check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_telegram(self, email):
        """Check Telegram account"""
        cache_key = f"tg_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        # Telegram doesn't have public email check API
        # This is a placeholder
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.5}
    
    def check_pinterest(self, email):
        """Check Pinterest account"""
        cache_key = f"pin_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.pinterest.com/reset/',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'email sent' in text or 'reset link' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"Pinterest check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_quora(self, email):
        """Check Quora account"""
        cache_key = f"qr_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.quora.com/contact',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'account exists' in text or 'already registered' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Quora check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_tumblr(self, email):
        """Check Tumblr account"""
        cache_key = f"tb_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://www.tumblr.com/forgot_password',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'reset link' in text or 'email sent' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Tumblr check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_flickr(self, email):
        """Check Flickr account"""
        cache_key = f"fl_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://identity.flickr.com/forgot-password',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'reset link' in text or 'email sent' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Flickr check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_wordpress(self, email):
        """Check WordPress.com account"""
        cache_key = f"wp_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://wordpress.com/wp-login.php?action=lostpassword',
                data={'user_login': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'reset link' in text or 'email sent' in text:
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.85}
        
        except Exception as e:
            self.logger.log('debug', f"WordPress check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_vk(self, email):
        """Check VK account"""
        cache_key = f"vk_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://vk.com/restore',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if 'восстановление' in text or 'восстановить' in text:  # Russian for "restore"
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"VK check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_weibo(self, email):
        """Check Weibo account"""
        cache_key = f"wb_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://weibo.com/signup',
                data={'email': email}
            )
            
            if response and response.status_code == 200:
                text = response.text.lower()
                
                if '已注册' in text or 'registered' in text:  # Chinese for "registered"
                    self.cache.set(cache_key, True)
                    return {'found': True, 'confidence': 0.8}
        
        except Exception as e:
            self.logger.log('debug', f"Weibo check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    def check_apple(self, email):
        """Check Apple/iCloud account"""
        cache_key = f"ap_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return {'found': cached, 'confidence': 0.9}
        
        try:
            response = self.network.smart_request(
                'POST',
                'https://appleid.apple.com/account/validation/appleid',
                json={'email': email}
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    if data.get('isValid', False):
                        self.cache.set(cache_key, True)
                        return {'found': True, 'confidence': 0.9}
                except:
                    pass
        
        except Exception as e:
            self.logger.log('debug', f"Apple check failed: {e}")
        
        self.cache.set(cache_key, False)
        return {'found': False, 'confidence': 0.7}
    
    # ========== SECURITY & REPUTATION CHECKS ==========
    
    def check_hibp(self, email):
        """Check Have I Been Pwned for breaches"""
        if not self.network.config.HIBP_API_KEY:
            return {'found': False, 'confidence': 0.5, 'metadata': {'error': 'API key missing'}}
        
        cache_key = f"hibp_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        
        try:
            headers = {
                'hibp-api-key': self.network.config.HIBP_API_KEY,
                'User-Agent': 'MegaEmailChecker'
            }
            
            response = self.network.smart_request(
                'GET',
                f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}',
                headers=headers,
                timeout=10
            )
            
            if response and response.status_code == 200:
                try:
                    breaches = response.json()
                    result = {
                        'found': True,
                        'confidence': 1.0,
                        'metadata': {
                            'breach_count': len(breaches),
                            'breaches': breaches[:5],  # First 5 breaches
                            'total_breaches': len(breaches)
                        }
                    }
                    self.cache.set(cache_key, result)
                    return result
                except:
                    pass
            elif response and response.status_code == 404:
                result = {
                    'found': False,
                    'confidence': 1.0,
                    'metadata': {'breach_count': 0}
                }
                self.cache.set(cache_key, result)
                return result
        
        except Exception as e:
            self.logger.log('debug', f"HIBP check failed: {e}")
        
        result = {'found': False, 'confidence': 0.5}
        self.cache.set(cache_key, result)
        return result
    
    def check_emailrep(self, email):
        """Check email reputation"""
        if not self.network.config.EMAILREP_API_KEY:
            return {'found': False, 'confidence': 0.5, 'metadata': {'error': 'API key missing'}}
        
        cache_key = f"emailrep_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        
        try:
            headers = {
                'Key': self.network.config.EMAILREP_API_KEY,
                'User-Agent': 'MegaEmailChecker'
            }
            
            response = self.network.smart_request(
                'GET',
                f'https://emailrep.io/{email}',
                headers=headers,
                timeout=10
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    result = {
                        'found': True,
                        'confidence': 0.9,
                        'metadata': data
                    }
                    self.cache.set(cache_key, result)
                    return result
                except:
                    pass
        
        except Exception as e:
            self.logger.log('debug', f"EmailRep check failed: {e}")
        
        result = {'found': False, 'confidence': 0.5}
        self.cache.set(cache_key, result)
        return result
    
    def check_hunter(self, email):
        """Check email with Hunter.io"""
        if not self.network.config.HIBP_API_KEY:  # Using same key for demo
            return {'found': False, 'confidence': 0.5, 'metadata': {'error': 'API key missing'}}
        
        cache_key = f"hunter_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        
        try:
            response = self.network.smart_request(
                'GET',
                f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={self.network.config.HIBP_API_KEY}',
                timeout=10
            )
            
            if response and response.status_code == 200:
                try:
                    data = response.json()
                    result = {
                        'found': data.get('data', {}).get('status') == 'valid',
                        'confidence': 0.9,
                        'metadata': data.get('data', {})
                    }
                    self.cache.set(cache_key, result)
                    return result
                except:
                    pass
        
        except Exception as e:
            self.logger.log('debug', f"Hunter check failed: {e}")
        
        result = {'found': False, 'confidence': 0.5}
        self.cache.set(cache_key, result)
        return result
    
    def check_dehashed(self, email):
        """Check DeHashed for breaches"""
        cache_key = f"dehashed_{hashlib.md5(email.encode()).hexdigest()[:16]}"
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached
        
        # Placeholder - actual implementation requires API key
        result = {'found': False, 'confidence': 0.5}
        self.cache.set(cache_key, result)
        return result

# ========== ADVANCED CHECKER CLASS ==========
class MegaEmailCheckerUltimatePro:
    def __init__(self):
        self.config = UltraConfig()
        self.logger = EnhancedLogger(self.config)
        self.validator = EnhancedEmailValidator()
        self.network = EnhancedNetworkEngine(self.config, self.logger)
        self.cache = EnhancedCacheEngine(self.config, self.logger)
        self.database = EnhancedDatabaseEngine(self.config, self.logger)
        self.services = AdvancedServiceCheckers(self.network, self.cache, self.logger)
        
        self.stats = {
            'total_emails': 0,
            'total_checks': 0,
            'successful_checks': 0,
            'failed_checks': 0,
            'start_time': time.time(),
            'peak_memory': 0,
            'requests_made': 0
        }
        
        self.running = False
        self.pause_event = threading.Event()
        self.pause_event.set()  # Start unpaused
        
    def show_banner(self):
        """Display enhanced banner with system info"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Get system info
        system_info = self.get_system_info()
        
        banner = f"""
{Fore.MAGENTA}
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓                                                                                                                         ▓
▓  {Fore.CYAN}╔╦╗┬┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┬┌─┐┬┌─┐  ╔═╗┌─┐┬─┐┌─┐┌─┐  ╦ ╦┌─┐┌─┐┬ ┬  ╔╗ ┌─┐┬ ┬┌┬┐┌─┐┬─┐{Fore.MAGENTA}                       ▓
▓  {Fore.CYAN} ║ ├┴┐├┤ ├─┤   ║║║├─┤│││├┤ ││ ┬│└─┐  ╠═╝├┤ ├┬┘└─┐├┤   ╠═╣├─┤│  ├─┤  ╠╩╗├─┤│ │ │ ├┤ ├┬┘{Fore.MAGENTA}                       ▓
▓  {Fore.CYAN} ╩ ┴ ┴└─┘┴ ┴  ═╩╝┴┴ ┴┘└┘└─┘┴└─┘┴└─┘  ╩  └─┘┴└─└─┘└─┘  ╩ ╩┴ ┴└─┘┴ ┴  ╚═╝┴ ┴└─┘ ┴ └─┘┴└─{Fore.MAGENTA}                       ▓
▓                                                                                                                         ▓
▓  {Fore.YELLOW}╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗{Fore.MAGENTA} ▓
▓  {Fore.YELLOW}║                                                                                                       ║{Fore.MAGENTA} ▓
▓  {Fore.YELLOW}║    {Fore.CYAN}🚀 MEGA EMAIL CHECKER {self.config.VERSION} - {self.config.AUTHOR}                          {Fore.YELLOW}║{Fore.MAGENTA} ▓
▓  {Fore.YELLOW}║    {Fore.GREEN}📞 Contact: {self.config.CONTACT}                                                         {Fore.YELLOW}║{Fore.MAGENTA} ▓
▓  {Fore.YELLOW}║    {Fore.CYAN}📅 Release: {self.config.RELEASE_DATE}                                                   {Fore.YELLOW}║{Fore.MAGENTA} ▓
▓  {Fore.YELLOW}║                                                                                                       ║{Fore.MAGENTA} ▓
▓  {Fore.YELLOW}╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝{Fore.MAGENTA} ▓
▓                                                                                                                         ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
{Style.RESET_ALL}
"""
        print(banner)
        
        # System info
        print(f"{Fore.CYAN}{'━'*70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🖥️  SYSTEM INFORMATION{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*70}{Style.RESET_ALL}")
        
        for key, value in system_info.items():
            print(f"{Fore.WHITE}{key:20}{Fore.CYAN}{value}{Style.RESET_ALL}")
        
        # Stats display
        cache_stats = self.cache.get_stats()
        proxy_stats = self.network.proxy_manager.get_proxy_stats()
        db_stats = self.database.get_dashboard_stats()
        
        print(f"\n{Fore.CYAN}{'━'*70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📊 CURRENT STATUS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*70}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}Services Available:{Fore.GREEN} {len(self.services.services)}")
        print(f"{Fore.WHITE}Proxies Working:{Fore.YELLOW} {proxy_stats['working']}/{proxy_stats['total']}")
        print(f"{Fore.WHITE}Cache Efficiency:{Fore.MAGENTA} {cache_stats['hit_rate']:.1f}% ({cache_stats['size']} entries)")
        print(f"{Fore.WHITE}Database Emails:{Fore.CYAN} {db_stats.get('total_emails', 0)}")
        print(f"{Fore.WHITE}Max Threads:{Fore.GREEN} {self.config.MAX_WORKERS}")
        print(f"{Fore.WHITE}Max Processes:{Fore.BLUE} {self.config.MAX_PROCESSES}")
        print(f"{Fore.WHITE}Encryption:{Fore.GREEN} {'Enabled' if self.config.ENABLE_ENCRYPTION else 'Disabled'}")
        print(f"{Fore.WHITE}Tor Proxy:{Fore.YELLOW} {'Enabled' if self.config.USE_TOR_PROXY else 'Disabled'}")
        
        if self.stats['total_emails'] > 0:
            print(f"\n{Fore.WHITE}Session Stats:{Style.RESET_ALL}")
            print(f"  Emails Checked: {Fore.CYAN}{self.stats['total_emails']}")
            print(f"  Total Checks: {Fore.YELLOW}{self.stats['total_checks']}")
            print(f"  Successful: {Fore.GREEN}{self.stats['successful_checks']}")
            print(f"  Uptime: {Fore.MAGENTA}{timedelta(seconds=int(time.time() - self.stats['start_time']))}")
        
        print()
    
    def get_system_info(self):
        """Get system information"""
        info = {}
        
        # System
        info['System'] = platform.system()
        info['Release'] = platform.release()
        info['Version'] = platform.version()
        info['Machine'] = platform.machine()
        info['Processor'] = platform.processor()
        
        # Python
        info['Python'] = platform.python_version()
        info['Python Compiler'] = platform.python_compiler()
        
        # CPU
        info['CPU Cores'] = psutil.cpu_count(logical=True)
        info['CPU Usage'] = f"{psutil.cpu_percent()}%"
        
        # Memory
        mem = psutil.virtual_memory()
        info['Memory Total'] = f"{mem.total / (1024**3):.1f} GB"
        info['Memory Used'] = f"{mem.used / (1024**3):.1f} GB ({mem.percent}%)"
        
        # Disk
        disk = psutil.disk_usage('/')
        info['Disk Total'] = f"{disk.total / (1024**3):.1f} GB"
        info['Disk Used'] = f"{disk.used / (1024**3):.1f} GB ({disk.percent}%)"
        
        return info
    
    def check_single_email(self, email):
        """Enhanced single email check with progress tracking"""
        if not self.validator.validate(email)['valid']:
            validation = self.validator.validate(email)
            self.logger.log('error', f"Invalid email: {email}")
            
            if validation['has_typo']:
                print(f"{Fore.YELLOW}[!] Possible typo detected. Did you mean: {validation['suggested_correction']}?{Style.RESET_ALL}")
            
            return None
        
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🔍 CHECKING:{Fore.CYAN} {email}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        start_time = time.time()
        validation_result = self.validator.validate(email)
        
        # Display email info
        print(f"{Fore.WHITE}📧 Email:{Fore.CYAN} {email}")
        print(f"{Fore.WHITE}🏷️  Domain:{Fore.YELLOW} {validation_result['domain']}")
        print(f"{Fore.WHITE}👤 Username:{Fore.MAGENTA} {validation_result['username']}")
        print(f"{Fore.WHITE}✅ Valid:{Fore.GREEN if validation_result['valid'] else Fore.RED} {validation_result['valid']}")
        
        if validation_result['has_typo']:
            print(f"{Fore.YELLOW}⚠️  Typo detected. Suggestion: {validation_result['suggested_correction']}")
        
        if validation_result['is_disposable']:
            print(f"{Fore.RED}⚠️  Disposable email detected")
        
        # Get email stats from database
        email_stats = self.database.get_email_stats(email)
        if email_stats.get('check_count', 0) > 0:
            print(f"{Fore.CYAN}[*] Previously checked {email_stats['check_count']} times")
            if email_stats.get('last_checked'):
                last_check = datetime.fromisoformat(email_stats['last_checked'].replace('Z', '+00:00'))
                print(f"{Fore.CYAN}[*] Last check: {last_check.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Sort services by priority
        sorted_services = sorted(
            self.services.services.items(),
            key=lambda x: x[1]["priority"]
        )
        
        # Process with ThreadPoolExecutor
        total_services = len(sorted_services)
        print(f"\n{Fore.CYAN}[*] Checking {total_services} services across {self.config.MAX_WORKERS} threads...{Style.RESET_ALL}")
        
        results = {}
        with ThreadPoolExecutor(max_workers=self.config.MAX_WORKERS) as executor:
            # Submit all tasks
            future_to_service = {}
            for service_name, service_info in sorted_services:
                if service_info.get('api_key_required', False) and not getattr(self.config, f"{service_name.upper()}_API_KEY", None):
                    self.logger.log('warning', f"Skipping {service_name}: API key required")
                    continue
                
                future = executor.submit(service_info["check_method"], email)
                future_to_service[future] = (service_name, service_info)
            
            # Process results with progress bar
            completed = 0
            with tqdm(total=total_services, desc="Checking services", unit="service", 
                     bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]") as pbar:
                
                for future in as_completed(future_to_service):
                    service_name, service_info = future_to_service[future]
                    
                    completed += 1
                    
                    try:
                        result = future.result(timeout=45)
                        results[service_name] = result
                        
                        # Update progress bar
                        emoji = service_info['emoji']
                        color = service_info['color']
                        category = service_info['category']
                        
                        if isinstance(result, dict):
                            found = result.get('found', False)
                            confidence = result.get('confidence', 0.5)
                        else:
                            found = result
                            confidence = 1.0
                        
                        status = f"{Fore.GREEN}✓" if found else f"{Fore.RED}✗"
                        pbar.set_postfix_str(f"{emoji} {service_name:15} {status} {confidence:.1f}")
                        pbar.update(1)
                        
                    except Exception as e:
                        self.logger.log('error', f"Error checking {service_name}: {e}")
                        results[service_name] = {'found': False, 'confidence': 0.0, 'error': str(e)}
                        pbar.update(1)
        
        elapsed_time = time.time() - start_time
        
        # Update stats
        self.stats['total_emails'] += 1
        self.stats['total_checks'] += total_services
        
        # Count successful finds
        found_count = 0
        for result in results.values():
            if isinstance(result, dict):
                if result.get('found', False):
                    found_count += 1
            elif result:
                found_count += 1
        
        self.stats['successful_checks'] += found_count
        
        # Display results
        self._display_enhanced_results(email, validation_result, results, elapsed_time, found_count)
        
        # Save to database
        self.database.save_email_result(email, validation_result, results, elapsed_time)
        
        # Save cache periodically
        if self.stats['total_emails'] % 10 == 0:
            self.cache.save_cache()
            self.cache.clear_expired()
        
        # Update memory usage
        current_memory = psutil.Process().memory_info().rss / (1024 * 1024)
        self.stats['peak_memory'] = max(self.stats['peak_memory'], current_memory)
        
        return results
    
    def check_batch_emails(self, emails, max_workers=None):
        """Enhanced batch email checking"""
        if not emails:
            self.logger.log('error', "No emails provided")
            return
        
        total_emails = len(emails)
        valid_emails = []
        
        # Validate emails first
        print(f"\n{Fore.CYAN}[*] Validating {total_emails} emails...{Style.RESET_ALL}")
        for email in emails:
            validation = self.validator.validate(email)
            if validation['valid']:
                valid_emails.append(email)
            else:
                self.logger.log('warning', f"Invalid email skipped: {email}")
        
        valid_count = len(valid_emails)
        print(f"{Fore.GREEN}[+] Found {valid_count} valid emails ({total_emails - valid_count} invalid skipped){Style.RESET_ALL}")
        
        if valid_count == 0:
            return
        
        results_summary = []
        start_time = time.time()
        
        # Use ProcessPoolExecutor for CPU-bound tasks
        with ProcessPoolExecutor(max_workers=min(self.config.MAX_PROCESSES, valid_count)) as executor:
            futures = {}
            
            for idx, email in enumerate(valid_emails):
                future = executor.submit(self._process_single_email_parallel, email, idx, valid_count)
                futures[future] = email
            
            # Process results as they complete
            for future in tqdm(as_completed(futures), total=valid_count, 
                             desc="Processing emails", unit="email"):
                email = futures[future]
                
                try:
                    result = future.result(timeout=300)  # 5 minutes timeout
                    if result:
                        results_summary.append(result)
                        
                        # Auto-save every 10 emails
                        if len(results_summary) % 10 == 0:
                            self._save_batch_progress(results_summary)
                
                except Exception as e:
                    self.logger.log('error', f"Failed to process {email}: {e}")
        
        total_time = time.time() - start_time
        
        # Display batch summary
        self._display_enhanced_batch_summary(results_summary, total_time)
        
        # Export results
        self._export_batch_results(results_summary)
    
    def _process_single_email_parallel(self, email, idx, total):
        """Process single email in parallel"""
        try:
            # Create local instances for parallel processing
            local_config = UltraConfig()
            local_logger = EnhancedLogger(local_config)
            local_network = EnhancedNetworkEngine(local_config, local_logger)
            local_cache = EnhancedCacheEngine(local_config, local_logger)
            local_services = AdvancedServiceCheckers(local_network, local_cache, local_logger)
            
            # Check email
            results = {}
            for service_name, service_info in local_services.services.items():
                try:
                    result = service_info["check_method"](email)
                    results[service_name] = result
                except:
                    results[service_name] = {'found': False, 'confidence': 0.0}
            
            # Count found services
            found_count = sum(1 for r in results.values() 
                            if (isinstance(r, dict) and r.get('found', False)) or 
                            (not isinstance(r, dict) and r))
            
            return {
                'email': email,
                'found_count': found_count,
                'total_services': len(results),
                'results': {k: (v['found'] if isinstance(v, dict) else v) 
                          for k, v in results.items()}
            }
            
        except Exception as e:
            self.logger.log('error', f"Parallel processing error for {email}: {e}")
            return None
    
    def _save_batch_progress(self, results_summary):
        """Save batch progress"""
        try:
            progress_file = f"batch_progress_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(progress_file, 'w') as f:
                json.dump(results_summary, f, indent=2, default=str)
            
            self.logger.log('info', f"Progress saved to {progress_file}")
        except Exception as e:
            self.logger.log('error', f"Progress save error: {e}")
    
    def check_from_file(self, filename=None, start_line=0, end_line=None):
        """Enhanced file checking with resume capability"""
        if not filename:
            filename = self.config.EMAILS_FILE
        
        if not os.path.exists(filename):
            self.logger.log('error', f"File not found: {filename}")
            self._create_sample_emails_file(filename)
            return
        
        # Check for resume file
        resume_file = f"{filename}.resume"
        if os.path.exists(resume_file):
            choice = input(f"\n{Fore.YELLOW}[!] Resume file found. Resume from last position? (y/n): {Style.RESET_ALL}")
            if choice.lower() == 'y':
                try:
                    with open(resume_file, 'r') as f:
                        resume_data = json.load(f)
                    start_line = resume_data.get('last_line', 0)
                    print(f"{Fore.GREEN}[+] Resuming from line {start_line}{Style.RESET_ALL}")
                except:
                    pass
        
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        emails = []
        for line_num, line in enumerate(lines[start_line:], start=start_line):
            line = line.strip()
            if line and '@' in line and not line.startswith('#'):
                # Try to extract email from line
                email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', line)
                if email_match:
                    emails.append(email_match.group(0))
            
            if end_line and line_num >= end_line:
                break
        
        if not emails:
            self.logger.log('error', "No valid emails found in file")
            return
        
        print(f"{Fore.GREEN}[+] Found {len(emails)} emails in {filename}{Style.RESET_ALL}")
        
        # Start checking
        self.check_batch_emails(emails)
        
        # Save resume position
        try:
            with open(resume_file, 'w') as f:
                json.dump({'last_line': len(lines)}, f)
        except:
            pass
    
    def _display_enhanced_results(self, email, validation, results, elapsed_time, found_count):
        """Display enhanced results"""
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📋 CHECK RESULTS SUMMARY{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        # Basic info
        print(f"{Fore.WHITE}📧 Email:{Fore.CYAN} {email}")
        print(f"{Fore.WHITE}⏱️  Time:{Fore.YELLOW} {elapsed_time:.2f} seconds")
        print(f"{Fore.WHITE}📅 Date:{Fore.CYAN} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Fore.WHITE}🏷️  Domain Type:{Fore.MAGENTA} {validation.get('domain_type', 'Unknown')}")
        
        # Calculate statistics
        total_services = len(results)
        success_rate = (found_count / total_services * 100) if total_services > 0 else 0
        
        print(f"\n{Fore.WHITE}📊 Statistics:{Style.RESET_ALL}")
        print(f"  Found: {Fore.GREEN}{found_count}{Style.RESET_ALL} / {total_services}")
        print(f"  Success Rate: {Fore.YELLOW}{success_rate:.1f}%{Style.RESET_ALL}")
        print(f"  Avg per service: {Fore.CYAN}{(elapsed_time/total_services):.2f}s{Style.RESET_ALL}")
        
        # Group by category
        categories = {}
        for service_name, result in results.items():
            if service_name in self.services.services:
                category = self.services.services[service_name]['category']
                if category not in categories:
                    categories[category] = []
                
                found = False
                confidence = 0.0
                
                if isinstance(result, dict):
                    found = result.get('found', False)
                    confidence = result.get('confidence', 0.0)
                else:
                    found = result
                    confidence = 1.0 if found else 0.0
                
                categories[category].append({
                    'name': service_name,
                    'found': found,
                    'confidence': confidence,
                    'emoji': self.services.services[service_name]['emoji'],
                    'color': self.services.services[service_name]['color']
                })
        
        # Display by category
        print(f"\n{Fore.YELLOW}📂 RESULTS BY CATEGORY:{Style.RESET_ALL}")
        
        for category, services in sorted(categories.items()):
            found_in_category = [s for s in services if s['found']]
            total_in_category = len(services)
            
            if total_in_category > 0:
                category_rate = (len(found_in_category) / total_in_category * 100)
                print(f"\n  {Fore.CYAN}{category}: {len(found_in_category)}/{total_in_category} ({category_rate:.1f}%){Style.RESET_ALL}")
                
                if found_in_category:
                    for service in found_in_category:
                        confidence_str = f"{Fore.WHITE}({service['confidence']:.1f}){Style.RESET_ALL}"
                        print(f"    {service['emoji']} {service['color']}{service['name']:20}{Style.RESET_ALL} {confidence_str}")
        
        # Security checks
        security_services = ['HaveIBeenPwned', 'EmailRep', 'Hunter.io', 'DeHashed']
        security_results = {}
        
        for service in security_services:
            if service in results:
                security_results[service] = results[service]
        
        if security_results:
            print(f"\n{Fore.YELLOW}🛡️  SECURITY CHECKS:{Style.RESET_ALL}")
            
            for service, result in security_results.items():
                if isinstance(result, dict):
                    found = result.get('found', False)
                    metadata = result.get('metadata', {})
                    
                    if service == 'HaveIBeenPwned' and found:
                        breach_count = metadata.get('breach_count', 0)
                        color = Fore.RED if breach_count > 0 else Fore.GREEN
                        print(f"    ⚠️  {service}: {color}{breach_count} breaches found{Style.RESET_ALL}")
                    
                    elif service == 'EmailRep' and found:
                        reputation = metadata.get('reputation', 'unknown')
                        print(f"    🛡️  {service}: Reputation - {reputation}")
        
        # Save to results file
        self._save_to_enhanced_results_file(email, results, elapsed_time, found_count, categories)
        
        print(f"\n{Fore.GREEN}[+] Results saved to database and results file{Style.RESET_ALL}")
    
    def _display_enhanced_batch_summary(self, results_summary, total_time):
        """Display enhanced batch summary"""
        if not results_summary:
            return
        
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📦 BATCH CHECK COMPLETE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        total_emails = len(results_summary)
        total_found = sum(r['found_count'] for r in results_summary)
        total_services = sum(r['total_services'] for r in results_summary)
        
        avg_found = total_found / total_emails if total_emails > 0 else 0
        avg_success_rate = (total_found / total_services * 100) if total_services > 0 else 0
        
        print(f"{Fore.WHITE}Total Emails:{Fore.CYAN} {total_emails}")
        print(f"{Fore.WHITE}Total Accounts Found:{Fore.GREEN} {total_found}")
        print(f"{Fore.WHITE}Average per Email:{Fore.YELLOW} {avg_found:.1f}")
        print(f"{Fore.WHITE}Overall Success Rate:{Fore.MAGENTA} {avg_success_rate:.1f}%")
        print(f"{Fore.WHITE}Total Time:{Fore.CYAN} {timedelta(seconds=int(total_time))}")
        print(f"{Fore.WHITE}Speed:{Fore.GREEN} {total_emails / total_time:.2f} emails/second")
        
        # Top emails with most accounts
        if results_summary:
            top_emails = sorted(results_summary, key=lambda x: x['found_count'], reverse=True)[:10]
            
            print(f"\n{Fore.CYAN}🏆 TOP 10 EMAILS:{Style.RESET_ALL}")
            for idx, item in enumerate(top_emails, 1):
                success_rate = (item['found_count'] / item['total_services'] * 100) if item['total_services'] > 0 else 0
                print(f"  {idx:2}. {item['email'][:30]:30} - {Fore.GREEN}{item['found_count']:3}{Style.RESET_ALL} accounts ({success_rate:.1f}%)")
            
            # Distribution
            print(f"\n{Fore.CYAN}📊 DISTRIBUTION:{Style.RESET_ALL}")
            distribution = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, '5+': 0}
            
            for item in results_summary:
                count = item['found_count']
                if count <= 4:
                    distribution[count] += 1
                else:
                    distribution['5+'] += 1
            
            for count, freq in distribution.items():
                if freq > 0:
                    percentage = (freq / total_emails * 100)
                    bar = '█' * int(percentage / 2)
                    print(f"  {count:>2} accounts: {freq:4} emails {bar}")
        
        # Most common services found
        service_counts = {}
        for item in results_summary:
            for service_name, found in item.get('results', {}).items():
                if found:
                    service_counts[service_name] = service_counts.get(service_name, 0) + 1
        
        if service_counts:
            top_services = sorted(service_counts.items(), key=lambda x: x[1], reverse=True)[:10]
            
            print(f"\n{Fore.CYAN}📱 MOST COMMON SERVICES:{Style.RESET_ALL}")
            for service, count in top_services:
                percentage = (count / total_emails * 100)
                print(f"  {service:20} - {count:4} emails ({percentage:.1f}%)")
    
    def _export_batch_results(self, results_summary):
        """Export batch results"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Export to CSV
        csv_file = f"batch_results_{timestamp}.csv"
        try:
            with open(csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Header
                headers = ['Email', 'Total Found', 'Total Services', 'Success Rate']
                
                # Add service columns
                if results_summary:
                    sample_results = results_summary[0].get('results', {})
                    for service in sample_results.keys():
                        headers.append(service)
                
                writer.writerow(headers)
                
                # Data
                for item in results_summary:
                    row = [
                        item['email'],
                        item['found_count'],
                        item['total_services'],
                        f"{(item['found_count'] / item['total_services'] * 100):.1f}%" if item['total_services'] > 0 else "0%"
                    ]
                    
                    # Add service results
                    for service in sample_results.keys():
                        row.append('✓' if item['results'].get(service, False) else '✗')
                    
                    writer.writerow(row)
            
            print(f"{Fore.GREEN}[+] Results exported to CSV: {csv_file}{Style.RESET_ALL}")
            
        except Exception as e:
            self.logger.log('error', f"CSV export error: {e}")
        
        # Export to JSON
        json_file = f"batch_results_{timestamp}.json"
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(results_summary, f, indent=2, default=str)
            
            print(f"{Fore.GREEN}[+] Results exported to JSON: {json_file}{Style.RESET_ALL}")
            
        except Exception as e:
            self.logger.log('error', f"JSON export error: {e}")
    
    def _save_to_enhanced_results_file(self, email, results, elapsed_time, found_count, categories):
        """Save results to enhanced results file"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(self.config.RESULTS_FILE, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*80}\n")
                f.write(f"📧 Email: {email}\n")
                f.write(f"⏰ Time: {timestamp}\n")
                f.write(f"⏱️  Duration: {elapsed_time:.2f}s\n")
                f.write(f"📊 Found: {found_count}/{len(results)} accounts\n")
                f.write(f"{'─'*40}\n")
                
                for category, services in categories.items():
                    found_in_category = [s for s in services if s['found']]
                    if found_in_category:
                        f.write(f"\n✅ {category}:\n")
                        for service in found_in_category:
                            f.write(f"  {service['emoji']} {service['name']}\n")
                
                f.write(f"{'='*80}\n")
            
        except Exception as e:
            self.logger.log('error', f"Results file save error: {e}")
    
    def show_dashboard(self):
        """Show enhanced dashboard"""
        self.show_banner()
        
        # Get statistics
        db_stats = self.database.get_dashboard_stats()
        cache_stats = self.cache.get_stats()
        proxy_stats = self.network.proxy_manager.get_proxy_stats()
        
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📈 DASHBOARD{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        # Overall stats
        print(f"{Fore.WHITE}📊 OVERALL STATISTICS:{Style.RESET_ALL}")
        print(f"  Total Emails: {Fore.CYAN}{db_stats.get('total_emails', 0):,}")
        print(f"  Total Checks: {Fore.YELLOW}{self.stats['total_checks']:,}")
        print(f"  Successful Finds: {Fore.GREEN}{self.stats['successful_checks']:,}")
        print(f"  Cache Hit Rate: {Fore.MAGENTA}{cache_stats['hit_rate']:.1f}%")
        print(f"  Working Proxies: {Fore.BLUE}{proxy_stats['working']}/{proxy_stats['total']}")
        
        # Recent activity
        print(f"\n{Fore.WHITE}📅 RECENT ACTIVITY:{Style.RESET_ALL}")
        print(f"  Checked Today: {Fore.CYAN}{db_stats.get('checked_today', 0)} emails")
        print(f"  Session Uptime: {Fore.YELLOW}{timedelta(seconds=int(time.time() - self.stats['start_time']))}")
        print(f"  Peak Memory: {Fore.RED}{self.stats['peak_memory']:.1f} MB")
        
        # Top domains
        if db_stats.get('top_domains'):
            print(f"\n{Fore.WHITE}🏷️  TOP DOMAINS:{Style.RESET_ALL}")
            for domain in db_stats['top_domains'][:5]:
                print(f"  {domain['domain']:30} - {Fore.CYAN}{domain['count']:6}{Style.RESET_ALL} emails")
        
        # Top services
        if db_stats.get('top_services'):
            print(f"\n{Fore.WHITE}📱 TOP SERVICES:{Style.RESET_ALL}")
            for service in db_stats['top_services'][:5]:
                print(f"  {service['service_name']:20} - {Fore.GREEN}{service['success_rate']:5.1f}%{Style.RESET_ALL} success rate")
        
        # System status
        print(f"\n{Fore.WHITE}⚙️  SYSTEM STATUS:{Style.RESET_ALL}")
        print(f"  Database: {Fore.GREEN}✓ Connected{Style.RESET_ALL}")
        print(f"  Cache: {Fore.GREEN}✓ {cache_stats['size']} entries{Style.RESET_ALL}")
        print(f"  Network: {Fore.GREEN if proxy_stats['working'] > 0 else Fore.RED}✓ {proxy_stats['working']} proxies{Style.RESET_ALL}")
        print(f"  Threads: {Fore.BLUE}{self.config.MAX_WORKERS} active{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
    
    def export_results(self, format='all', query=None):
        """Enhanced export with multiple formats"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format in ['csv', 'all']:
            filename = f"export_{timestamp}.csv"
            if self.database.export_to_csv(filename, query):
                print(f"{Fore.GREEN}[+] Exported to CSV: {filename}{Style.RESET_ALL}")
        
        if format in ['json', 'all']:
            filename = f"export_{timestamp}.json"
            try:
                # Get data from database
                cursor = self.database.conn.cursor()
                
                if query:
                    cursor.execute(query)
                else:
                    cursor.execute('''
                        SELECT 
                            e.email,
                            e.domain,
                            e.is_valid,
                            e.is_disposable,
                            e.breach_count,
                            e.reputation_score,
                            e.last_checked,
                            json_group_array(
                                json_object(
                                    'service', r.service_name,
                                    'found', r.is_found,
                                    'confidence', r.confidence
                                )
                            ) as results
                        FROM emails e
                        LEFT JOIN results r ON e.id = r.email_id
                        GROUP BY e.email
                        ORDER BY e.last_checked DESC
                    ''')
                
                rows = cursor.fetchall()
                data = [dict(row) for row in rows]
                
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, default=str)
                
                print(f"{Fore.GREEN}[+] Exported to JSON: {filename}{Style.RESET_ALL}")
                
            except Exception as e:
                self.logger.log('error', f"JSON export error: {e}")
        
        if format in ['html', 'all']:
            filename = f"export_{timestamp}.html"
            self._export_to_html(filename, query)
            print(f"{Fore.GREEN}[+] Exported to HTML: {filename}{Style.RESET_ALL}")
    
    def _export_to_html(self, filename, query=None):
        """Export to HTML format"""
        try:
            # Get data
            cursor = self.database.conn.cursor()
            
            if query:
                cursor.execute(query)
            else:
                cursor.execute('''
                    SELECT 
                        e.email,
                        e.domain,
                        e.is_valid,
                        e.is_disposable,
                        e.breach_count,
                        e.reputation_score,
                        e.last_checked,
                        COUNT(r.id) as total_checks,
                        SUM(CASE WHEN r.is_found = 1 THEN 1 ELSE 0 END) as found_count
                    FROM emails e
                    LEFT JOIN results r ON e.id = r.email_id
                    GROUP BY e.email
                    ORDER BY e.last_checked DESC
                    LIMIT 1000
                ''')
            
            rows = cursor.fetchall()
            data = [dict(row) for row in rows]
            
            # Generate HTML
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Mega Email Checker Export - {datetime.now().strftime('%Y-%m-%d')}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
                    .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                    h1 {{ color: #333; border-bottom: 2px solid #4CAF50; padding-bottom: 10px; }}
                    table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                    th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
                    th {{ background-color: #4CAF50; color: white; }}
                    tr:hover {{ background-color: #f5f5f5; }}
                    .valid {{ color: green; font-weight: bold; }}
                    .invalid {{ color: red; }}
                    .disposable {{ color: orange; }}
                    .breach {{ color: darkred; }}
                    .stats {{ background: #e8f5e9; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>📧 Mega Email Checker Export</h1>
                    <div class="stats">
                        <strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br>
                        <strong>Total Records:</strong> {len(data)}<br>
                        <strong>Tool Version:</strong> {self.config.VERSION}
                    </div>
                    <table>
                        <thead>
                            <tr>
                                <th>Email</th>
                                <th>Domain</th>
                                <th>Status</th>
                                <th>Breaches</th>
                                <th>Reputation</th>
                                <th>Checks</th>
                                <th>Found</th>
                                <th>Last Checked</th>
                            </tr>
                        </thead>
                        <tbody>
            """
            
            for item in data:
                status_class = "valid" if item['is_valid'] else "invalid"
                status_text = "Valid" if item['is_valid'] else "Invalid"
                
                if item['is_disposable']:
                    status_class = "disposable"
                    status_text = "Disposable"
                
                breach_text = str(item['breach_count']) if item['breach_count'] > 0 else "0"
                breach_class = "breach" if item['breach_count'] > 0 else ""
                
                html_content += f"""
                            <tr>
                                <td>{item['email']}</td>
                                <td>{item['domain']}</td>
                                <td class="{status_class}">{status_text}</td>
                                <td class="{breach_class}">{breach_text}</td>
                                <td>{item['reputation_score'] or 'N/A'}</td>
                                <td>{item['total_checks']}</td>
                                <td>{item['found_count']}</td>
                                <td>{item['last_checked'] or 'Never'}</td>
                            </tr>
                """
            
            html_content += """
                        </tbody>
                    </table>
                </div>
            </body>
            </html>
            """
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
                
        except Exception as e:
            self.logger.log('error', f"HTML export error: {e}")
    
    def interactive_menu(self):
        """Enhanced interactive menu"""
        while True:
            self.show_banner()
            
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}          ULTRA VIP MENU{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            print(f"{Fore.WHITE}[1]  {Fore.GREEN}🔍 Check Single Email{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[2]  {Fore.BLUE}📋 Check Multiple Emails{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[3]  {Fore.CYAN}📁 Check From File{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[4]  {Fore.MAGENTA}🚀 Batch Check (Parallel){Style.RESET_ALL}")
            print(f"{Fore.WHITE}[5]  {Fore.YELLOW}📊 View Dashboard{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[6]  {Fore.CYAN}📈 View Statistics{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[7]  {Fore.GREEN}💾 Export Results{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[8]  {Fore.BLUE}🔍 Search Database{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[9]  {Fore.MAGENTA}⚙️  Settings{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[10] {Fore.RED}🛠️  Tools{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[11] {Fore.YELLOW}❌ Exit{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            try:
                choice = input(f"\n{Fore.WHITE}Select option (1-11): {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    email = input(f"\n{Fore.WHITE}Enter email: {Style.RESET_ALL}").strip()
                    if email:
                        self.check_single_email(email)
                    input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
                
                elif choice == '2':
                    print(f"\n{Fore.CYAN}[*] Enter emails (comma separated or one per line, end with empty line){Style.RESET_ALL}")
                    emails = []
                    while True:
                        line = input(f"{Fore.WHITE}Email {len(emails) + 1}: {Style.RESET_ALL}").strip()
                        if not line:
                            break
                        
                        if ',' in line:
                            emails.extend([e.strip() for e in line.split(',') if e.strip()])
                        else:
                            emails.append(line)
                    
                    if emails:
                        self.check_batch_emails(emails)
                    input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
                
                elif choice == '3':
                    filename = input(f"\n{Fore.WHITE}Filename (default: emails.txt): {Style.RESET_ALL}").strip()
                    if not filename:
                        filename = self.config.EMAILS_FILE
                    
                    start_line = input(f"{Fore.WHITE}Start from line (default: 0): {Style.RESET_ALL}").strip()
                    start_line = int(start_line) if start_line.isdigit() else 0
                    
                    end_line = input(f"{Fore.WHITE}End at line (default: all): {Style.RESET_ALL}").strip()
                    end_line = int(end_line) if end_line.isdigit() else None
                    
                    self.check_from_file(filename, start_line, end_line)
                    input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
                
                elif choice == '4':
                    filename = input(f"\n{Fore.WHITE}Filename for batch processing: {Style.RESET_ALL}").strip()
                    if not filename:
                        filename = self.config.EMAILS_FILE
                    
                    workers = input(f"{Fore.WHITE}Max workers (default: {self.config.MAX_PROCESSES}): {Style.RESET_ALL}").strip()
                    if workers.isdigit():
                        self.config.MAX_PROCESSES = int(workers)
                    
                    self.check_from_file(filename)
                    input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
                
                elif choice == '5':
                    self.show_dashboard()
                
                elif choice == '6':
                    self.show_statistics()
                    input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
                
                elif choice == '7':
                    print(f"\n{Fore.CYAN}[*] Select export format:{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[1] {Fore.GREEN}CSV{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[2] {Fore.BLUE}JSON{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[3] {Fore.YELLOW}HTML{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[4] {Fore.MAGENTA}All Formats{Style.RESET_ALL}")
                    
                    format_choice = input(f"\n{Fore.WHITE}Select format: {Style.RESET_ALL}").strip()
                    formats = {'1': 'csv', '2': 'json', '3': 'html', '4': 'all'}
                    export_format = formats.get(format_choice, 'all')
                    
                    # Advanced query option
                    use_query = input(f"{Fore.WHITE}Use custom SQL query? (y/n): {Style.RESET_ALL}").lower() == 'y'
                    query = None
                    if use_query:
                        query = input(f"{Fore.WHITE}Enter SQL query: {Style.RESET_ALL}").strip()
                    
                    self.export_results(export_format, query)
                    input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
                
                elif choice == '8':
                    self.search_database()
                
                elif choice == '9':
                    self.enhanced_settings_menu()
                
                elif choice == '10':
                    self.tools_menu()
                
                elif choice == '11':
                    print(f"\n{Fore.GREEN}[*] Thank you for using Mega Email Checker Ultra VIP!{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}[*] Total emails checked: {self.stats['total_emails']}{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}[*] Session duration: {timedelta(seconds=int(time.time() - self.stats['start_time']))}{Style.RESET_ALL}")
                    
                    # Save and cleanup
                    self.cache.save_cache()
                    self.database.conn.close()
                    
                    break
                
                else:
                    print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
                    time.sleep(1)
            
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}[*] Exiting...{Style.RESET_ALL}")
                self.cache.save_cache()
                self.database.conn.close()
                break
            except Exception as e:
                print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
                time.sleep(2)
    
    def search_database(self):
        """Search database with advanced filters"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          DATABASE SEARCH{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        query = {}
        
        # Build search query
        email_part = input(f"{Fore.WHITE}Email contains (leave empty for any): {Style.RESET_ALL}").strip()
        if email_part:
            query['email'] = email_part
        
        domain = input(f"{Fore.WHITE}Domain (leave empty for any): {Style.RESET_ALL}").strip()
        if domain:
            query['domain'] = domain
        
        valid_choice = input(f"{Fore.WHITE}Valid emails only? (y/n): {Style.RESET_ALL}").strip().lower()
        if valid_choice == 'y':
            query['is_valid'] = True
        elif valid_choice == 'n':
            query['is_valid'] = False
        
        breach_choice = input(f"{Fore.WHITE}With breaches only? (y/n): {Style.RESET_ALL}").strip().lower()
        if breach_choice == 'y':
            query['has_breaches'] = True
        
        service = input(f"{Fore.WHITE}Found on specific service (leave empty for any): {Style.RESET_ALL}").strip()
        if service:
            query['service'] = service
        
        limit = input(f"{Fore.WHITE}Max results (default: 100): {Style.RESET_ALL}").strip()
        limit = int(limit) if limit.isdigit() else 100
        
        # Search
        results = self.database.search_emails(query, limit)
        
        if results:
            print(f"\n{Fore.GREEN}[+] Found {len(results)} emails:{Style.RESET_ALL}")
            
            for idx, email in enumerate(results[:20], 1):  # Show first 20
                print(f"{idx:3}. {email['email']} - {email.get('found_count', 0)} accounts")
            
            if len(results) > 20:
                print(f"{Fore.CYAN}[...] and {len(results) - 20} more{Style.RESET_ALL}")
            
            # Export option
            export = input(f"\n{Fore.WHITE}Export results? (y/n): {Style.RESET_ALL}").strip().lower()
            if export == 'y':
                self.export_results('csv')
        else:
            print(f"{Fore.YELLOW}[!] No emails found{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Style.RESET_ALL}")
    
    def enhanced_settings_menu(self):
        """Enhanced settings menu"""
        while True:
            print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}          ENHANCED SETTINGS{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            cache_stats = self.cache.get_stats()
            proxy_stats = self.network.proxy_manager.get_proxy_stats()
            
            print(f"{Fore.WHITE}[1]  {Fore.CYAN}Cache: {cache_stats['size']} entries ({cache_stats['hit_rate']:.1f}% hit rate){Style.RESET_ALL}")
            print(f"{Fore.WHITE}[2]  {Fore.YELLOW}Proxies: {proxy_stats['working']}/{proxy_stats['total']} working{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[3]  {Fore.GREEN}Performance: {self.config.MAX_WORKERS} threads, {self.config.MAX_PROCESSES} processes{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[4]  {Fore.BLUE}Security: {'Encrypted' if self.config.ENABLE_ENCRYPTION else 'Plain'}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[5]  {Fore.MAGENTA}Network: Timeout {self.config.TIMEOUT}s, Retries {self.config.MAX_RETRIES}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[6]  {Fore.CYAN}Clear Cache{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[7]  {Fore.YELLOW}Update Proxies{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[8]  {Fore.GREEN}Test All Services{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[9]  {Fore.BLUE}Backup Database{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[10] {Fore.MAGENTA}Restore Database{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[11] {Fore.CYAN}API Keys{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[12] {Fore.YELLOW}Back to Main Menu{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.WHITE}Select option: {Style.RESET_ALL}").strip()
            
            if choice == '1':
                print(f"\n{Fore.CYAN}[*] Cache Statistics:{Style.RESET_ALL}")
                for key, value in cache_stats.items():
                    print(f"  {key:15}: {value}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '2':
                print(f"\n{Fore.CYAN}[*] Proxy Statistics:{Style.RESET_ALL}")
                print(f"  Total: {proxy_stats['total']}")
                print(f"  Working: {proxy_stats['working']}")
                print(f"  Banned: {proxy_stats['banned']}")
                
                if proxy_stats['working'] > 0:
                    print(f"\n{Fore.YELLOW}[*] First 5 working proxies:{Style.RESET_ALL}")
                    for i, proxy in enumerate(list(proxy_stats['stats'].keys())[:5], 1):
                        print(f"  {i}. {proxy}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '3':
                try:
                    threads = input(f"\n{Fore.WHITE}Enter thread count (1-100): {Style.RESET_ALL}").strip()
                    if threads.isdigit() and 1 <= int(threads) <= 100:
                        self.config.MAX_WORKERS = int(threads)
                        print(f"{Fore.GREEN}[✓] Threads updated to {threads}{Style.RESET_ALL}")
                    
                    processes = input(f"{Fore.WHITE}Enter process count (1-10): {Style.RESET_ALL}").strip()
                    if processes.isdigit() and 1 <= int(processes) <= 10:
                        self.config.MAX_PROCESSES = int(processes)
                        print(f"{Fore.GREEN}[✓] Processes updated to {processes}{Style.RESET_ALL}")
                except:
                    print(f"{Fore.RED}[!] Invalid input{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '4':
                self.config.ENABLE_ENCRYPTION = not self.config.ENABLE_ENCRYPTION
                status = "Enabled" if self.config.ENABLE_ENCRYPTION else "Disabled"
                print(f"{Fore.GREEN}[✓] Encryption {status}{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '5':
                try:
                    timeout = input(f"\n{Fore.WHITE}Enter timeout in seconds (10-60): {Style.RESET_ALL}").strip()
                    if timeout.isdigit() and 10 <= int(timeout) <= 60:
                        self.config.TIMEOUT = int(timeout)
                        print(f"{Fore.GREEN}[✓] Timeout updated to {timeout}s{Style.RESET_ALL}")
                    
                    retries = input(f"{Fore.WHITE}Enter max retries (1-10): {Style.RESET_ALL}").strip()
                    if retries.isdigit() and 1 <= int(retries) <= 10:
                        self.config.MAX_RETRIES = int(retries)
                        print(f"{Fore.GREEN}[✓] Retries updated to {retries}{Style.RESET_ALL}")
                except:
                    print(f"{Fore.RED}[!] Invalid input{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '6':
                confirm = input(f"\n{Fore.RED}[!] Clear all cache? (y/n): {Style.RESET_ALL}").lower()
                if confirm == 'y':
                    self.cache.cache = {}
                    self.cache.stats = {'hits': 0, 'misses': 0, 'size': 0}
                    self.cache.save_cache()
                    print(f"{Fore.GREEN}[✓] Cache cleared!{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '7':
                print(f"\n{Fore.YELLOW}[*] Updating proxies...{Style.RESET_ALL}")
                self.network.proxy_manager.load_proxies()
                print(f"{Fore.GREEN}[✓] Proxies updated: {len(self.network.proxy_manager.proxies)} loaded{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '8':
                self.test_all_services()
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '9':
                self.database.create_backup()
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '10':
                self.restore_database()
                input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
            
            elif choice == '11':
                self.api_keys_menu()
            
            elif choice == '12':
                break
            
            else:
                print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
                time.sleep(1)
    
    def tools_menu(self):
        """Tools menu"""
        while True:
            print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}          TOOLS{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            print(f"{Fore.WHITE}[1]  {Fore.GREEN}📧 Email Validator{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[2]  {Fore.BLUE}🌐 Proxy Tester{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[3]  {Fore.CYAN}🔍 Service Tester{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[4]  {Fore.YELLOW}📊 Report Generator{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[5]  {Fore.MAGENTA}🔄 Data Cleaner{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[6]  {Fore.CYAN}📈 Performance Monitor{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[7]  {Fore.GREEN}Back to Main Menu{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.WHITE}Select option: {Style.RESET_ALL}").strip()
            
            if choice == '1':
                self.email_validator_tool()
            
            elif choice == '2':
                self.proxy_tester_tool()
            
            elif choice == '3':
                self.service_tester_tool()
            
            elif choice == '4':
                self.report_generator_tool()
            
            elif choice == '5':
                self.data_cleaner_tool()
            
            elif choice == '6':
                self.performance_monitor_tool()
            
            elif choice == '7':
                break
            
            else:
                print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
                time.sleep(1)
    
    def email_validator_tool(self):
        """Email validator tool"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          EMAIL VALIDATOR{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        email = input(f"{Fore.WHITE}Enter email to validate: {Style.RESET_ALL}").strip()
        
        if email:
            result = self.validator.validate(email)
            
            print(f"\n{Fore.CYAN}[*] Validation Results:{Style.RESET_ALL}")
            for key, value in result.items():
                if isinstance(value, bool):
                    color = Fore.GREEN if value else Fore.RED
                    print(f"  {key:20}: {color}{value}{Style.RESET_ALL}")
                elif isinstance(value, list):
                    print(f"  {key:20}: {', '.join(value[:3])}" + ("..." if len(value) > 3 else ""))
                else:
                    print(f"  {key:20}: {value}")
            
            # Check patterns
            patterns = self.validator.extract_common_patterns(email)
            print(f"\n{Fore.CYAN}[*] Pattern Analysis:{Style.RESET_ALL}")
            for key, value in patterns.items():
                print(f"  {key:20}: {value}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def proxy_tester_tool(self):
        """Proxy tester tool"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          PROXY TESTER{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        proxy = input(f"{Fore.WHITE}Enter proxy (format: protocol://ip:port): {Style.RESET_ALL}").strip()
        
        if proxy:
            print(f"\n{Fore.YELLOW}[*] Testing proxy {proxy}...{Style.RESET_ALL}")
            
            try:
                session = requests.Session()
                session.proxies = {'http': proxy, 'https': proxy}
                session.timeout = 10
                
                start = time.time()
                response = session.get('http://httpbin.org/ip')
                elapsed = time.time() - start
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"{Fore.GREEN}[✓] Proxy working!{Style.RESET_ALL}")
                    print(f"  IP: {data.get('origin')}")
                    print(f"  Response time: {elapsed:.2f}s")
                    print(f"  Status: {response.status_code}")
                else:
                    print(f"{Fore.RED}[✗] Proxy failed{Style.RESET_ALL}")
                    print(f"  Status: {response.status_code}")
                    
            except Exception as e:
                print(f"{Fore.RED}[✗] Proxy error: {e}{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def service_tester_tool(self):
        """Service tester tool"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          SERVICE TESTER{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}Available services:{Style.RESET_ALL}")
        services = list(self.services.services.keys())
        
        for i in range(0, len(services), 4):
            row = services[i:i+4]
            print("  " + "  ".join(f"{idx+1:2}. {service:15}" for idx, service in enumerate(row, start=i)))
        
        choice = input(f"\n{Fore.WHITE}Select service number (or 'all'): {Style.RESET_ALL}").strip()
        
        if choice.lower() == 'all':
            services_to_test = services
        elif choice.isdigit() and 1 <= int(choice) <= len(services):
            services_to_test = [services[int(choice) - 1]]
        else:
            print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
            return
        
        test_email = input(f"{Fore.WHITE}Test email: {Style.RESET_ALL}").strip() or "test@example.com"
        
        print(f"\n{Fore.YELLOW}[*] Testing {len(services_to_test)} services...{Style.RESET_ALL}")
        
        results = []
        for service_name in services_to_test:
            if service_name in self.services.services:
                method = self.services.services[service_name]['check_method']
                
                try:
                    start = time.time()
                    result = method(test_email)
                    elapsed = time.time() - start
                    
                    if isinstance(result, dict):
                        found = result.get('found', False)
                        confidence = result.get('confidence', 0.0)
                    else:
                        found = result
                        confidence = 1.0
                    
                    results.append({
                        'service': service_name,
                        'found': found,
                        'confidence': confidence,
                        'time': elapsed,
                        'status': 'Success'
                    })
                    
                    color = Fore.GREEN if found else Fore.RED
                    print(f"  {color}{service_name:20} {elapsed:.2f}s  confidence: {confidence:.1f}{Style.RESET_ALL}")
                    
                except Exception as e:
                    results.append({
                        'service': service_name,
                        'found': False,
                        'confidence': 0.0,
                        'time': 0,
                        'status': f'Error: {e}'
                    })
                    print(f"  {Fore.RED}{service_name:20} Error: {e}{Style.RESET_ALL}")
        
        # Summary
        success_count = sum(1 for r in results if r['status'] == 'Success')
        avg_time = sum(r['time'] for r in results if r['status'] == 'Success') / success_count if success_count > 0 else 0
        
        print(f"\n{Fore.CYAN}[*] Summary: {success_count}/{len(services_to_test)} successful, avg time: {avg_time:.2f}s{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def report_generator_tool(self):
        """Report generator tool"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          REPORT GENERATOR{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        report_types = {
            '1': 'Daily Summary',
            '2': 'Service Performance',
            '3': 'Domain Analysis',
            '4': 'Security Report',
            '5': 'Custom Report'
        }
        
        for key, value in report_types.items():
            print(f"{Fore.WHITE}[{key}] {value}{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.WHITE}Select report type: {Style.RESET_ALL}").strip()
        
        if choice in report_types:
            report_name = report_types[choice]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"report_{report_name.lower().replace(' ', '_')}_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Report: {report_name}\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Tool: {self.config.VERSION}\n")
                f.write("="*80 + "\n\n")
                
                # Add report content based on type
                if choice == '1':
                    stats = self.database.get_dashboard_stats()
                    f.write("DAILY SUMMARY REPORT\n")
                    f.write("-"*40 + "\n")
                    for key, value in stats.items():
                        f.write(f"{key}: {value}\n")
                
                elif choice == '2':
                    cursor = self.database.conn.cursor()
                    cursor.execute('''
                        SELECT service_name, COUNT(*) as total, 
                               SUM(CASE WHEN is_found = 1 THEN 1 ELSE 0 END) as found,
                               AVG(check_time) as avg_time
                        FROM results 
                        GROUP BY service_name 
                        ORDER BY found DESC
                    ''')
                    
                    f.write("SERVICE PERFORMANCE REPORT\n")
                    f.write("-"*40 + "\n")
                    for row in cursor.fetchall():
                        f.write(f"{row[0]}: {row[2]}/{row[1]} found, avg time: {row[3]:.2f}s\n")
                
                elif choice == '3':
                    cursor = self.database.conn.cursor()
                    cursor.execute('''
                        SELECT domain, COUNT(*) as count,
                               AVG(breach_count) as avg_breaches
                        FROM emails 
                        GROUP BY domain 
                        ORDER BY count DESC 
                        LIMIT 20
                    ''')
                    
                    f.write("DOMAIN ANALYSIS REPORT\n")
                    f.write("-"*40 + "\n")
                    for row in cursor.fetchall():
                        f.write(f"{row[0]}: {row[1]} emails, avg breaches: {row[2]:.1f}\n")
                
                elif choice == '4':
                    cursor = self.database.conn.cursor()
                    cursor.execute('''
                        SELECT COUNT(*) as total_emails,
                               SUM(CASE WHEN breach_count > 0 THEN 1 ELSE 0 END) as breached,
                               SUM(CASE WHEN is_disposable = 1 THEN 1 ELSE 0 END) as disposable
                        FROM emails
                    ''')
                    
                    row = cursor.fetchone()
                    f.write("SECURITY REPORT\n")
                    f.write("-"*40 + "\n")
                    f.write(f"Total emails: {row[0]}\n")
                    f.write(f"Breached emails: {row[1]} ({row[1]/row[0]*100:.1f}%)\n")
                    f.write(f"Disposable emails: {row[2]} ({row[2]/row[0]*100:.1f}%)\n")
                
                elif choice == '5':
                    query = input(f"{Fore.WHITE}Enter custom SQL query: {Style.RESET_ALL}").strip()
                    if query:
                        try:
                            cursor = self.database.conn.cursor()
                            cursor.execute(query)
                            
                            f.write("CUSTOM REPORT\n")
                            f.write("-"*40 + "\n")
                            f.write(f"Query: {query}\n\n")
                            
                            for row in cursor.fetchall():
                                f.write(str(row) + "\n")
                        except Exception as e:
                            f.write(f"Error: {e}\n")
            
            print(f"{Fore.GREEN}[+] Report generated: {filename}{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def data_cleaner_tool(self):
        """Data cleaner tool"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          DATA CLEANER{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}[1] Remove duplicate emails{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[2] Remove invalid emails{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[3] Remove disposable emails{Style.RESET_ALL}")
        print(f"{Fore.WHITE}[4] Remove old records (older than 30 days){Style.RESET_ALL}")
        print(f"{Fore.WHITE}[5] Clean all{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.WHITE}Select option: {Style.RESET_ALL}").strip()
        
        if choice in ['1', '2', '3', '4', '5']:
            confirm = input(f"\n{Fore.RED}[!] This action cannot be undone. Continue? (y/n): {Style.RESET_ALL}").lower()
            
            if confirm == 'y':
                cursor = self.database.conn.cursor()
                
                if choice == '1' or choice == '5':
                    # Remove duplicates
                    cursor.execute('''
                        DELETE FROM emails 
                        WHERE id NOT IN (
                            SELECT MIN(id) 
                            FROM emails 
                            GROUP BY email
                        )
                    ''')
                    print(f"{Fore.GREEN}[✓] Duplicates removed{Style.RESET_ALL}")
                
                if choice == '2' or choice == '5':
                    # Remove invalid
                    cursor.execute("DELETE FROM emails WHERE is_valid = 0")
                    print(f"{Fore.GREEN}[✓] Invalid emails removed{Style.RESET_ALL}")
                
                if choice == '3' or choice == '5':
                    # Remove disposable
                    cursor.execute("DELETE FROM emails WHERE is_disposable = 1")
                    print(f"{Fore.GREEN}[✓] Disposable emails removed{Style.RESET_ALL}")
                
                if choice == '4' or choice == '5':
                    # Remove old records
                    cursor.execute("DELETE FROM emails WHERE last_checked < datetime('now', '-30 days')")
                    print(f"{Fore.GREEN}[✓] Old records removed{Style.RESET_ALL}")
                
                self.database.conn.commit()
                print(f"{Fore.GREEN}[✓] Cleanup complete{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def performance_monitor_tool(self):
        """Performance monitor tool"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          PERFORMANCE MONITOR{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        # System info
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        print(f"{Fore.WHITE}SYSTEM:{Style.RESET_ALL}")
        print(f"  CPU Usage: {Fore.GREEN}{cpu_percent}%{Style.RESET_ALL}")
        print(f"  Memory: {Fore.BLUE}{memory.percent}% used ({memory.used / (1024**3):.1f} GB / {memory.total / (1024**3):.1f} GB){Style.RESET_ALL}")
        print(f"  Disk: {Fore.YELLOW}{disk.percent}% used ({disk.used / (1024**3):.1f} GB / {disk.total / (1024**3):.1f} GB){Style.RESET_ALL}")
        
        # Application info
        process = psutil.Process()
        app_memory = process.memory_info().rss / (1024**3)
        app_threads = process.num_threads()
        
        print(f"\n{Fore.WHITE}APPLICATION:{Style.RESET_ALL}")
        print(f"  Memory Usage: {Fore.CYAN}{app_memory:.2f} GB{Style.RESET_ALL}")
        print(f"  Threads: {Fore.MAGENTA}{app_threads}{Style.RESET_ALL}")
        print(f"  Uptime: {Fore.GREEN}{timedelta(seconds=int(time.time() - self.stats['start_time']))}{Style.RESET_ALL}")
        
        # Network info
        print(f"\n{Fore.WHITE}NETWORK:{Style.RESET_ALL}")
        print(f"  Requests Made: {Fore.YELLOW}{self.stats.get('requests_made', 0)}{Style.RESET_ALL}")
        print(f"  Proxies Working: {Fore.BLUE}{len(self.network.proxy_manager.working_proxies)}/{len(self.network.proxy_manager.proxies)}{Style.RESET_ALL}")
        
        # Database info
        cursor = self.database.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM emails")
        email_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM results")
        result_count = cursor.fetchone()[0]
        
        print(f"\n{Fore.WHITE}DATABASE:{Style.RESET_ALL}")
        print(f"  Emails: {Fore.GREEN}{email_count}{Style.RESET_ALL}")
        print(f"  Results: {Fore.BLUE}{result_count}{Style.RESET_ALL}")
        print(f"  Avg Results per Email: {Fore.CYAN}{result_count/email_count if email_count > 0 else 0:.1f}{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def api_keys_menu(self):
        """API keys management menu"""
        while True:
            print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}          API KEYS MANAGEMENT{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
            
            print(f"{Fore.WHITE}[1] HaveIBeenPwned API Key: {Fore.CYAN}{'Set' if self.config.HIBP_API_KEY else 'Not Set'}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[2] EmailRep API Key: {Fore.CYAN}{'Set' if self.config.EMAILREP_API_KEY else 'Not Set'}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[3] Hunter.io API Key: {Fore.CYAN}{'Set' if self.config.HIBP_API_KEY else 'Not Set'}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[4} Test All API Keys{Style.RESET_ALL}")
            print(f"{Fore.WHITE}[5} Back{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.WHITE}Select option: {Style.RESET_ALL}").strip()
            
            if choice == '1':
                key = input(f"{Fore.WHITE}Enter HaveIBeenPwned API Key: {Style.RESET_ALL}").strip()
                if key:
                    self.config.HIBP_API_KEY = key
                    print(f"{Fore.GREEN}[✓] API Key set{Style.RESET_ALL}")
            
            elif choice == '2':
                key = input(f"{Fore.WHITE}Enter EmailRep API Key: {Style.RESET_ALL}").strip()
                if key:
                    self.config.EMAILREP_API_KEY = key
                    print(f"{Fore.GREEN}[✓] API Key set{Style.RESET_ALL}")
            
            elif choice == '3':
                key = input(f"{Fore.WHITE}Enter Hunter.io API Key: {Style.RESET_ALL}").strip()
                if key:
                    # Using same config for demo
                    self.config.HIBP_API_KEY = key
                    print(f"{Fore.GREEN}[✓] API Key set{Style.RESET_ALL}")
            
            elif choice == '4':
                self.test_api_keys()
            
            elif choice == '5':
                break
            
            else:
                print(f"{Fore.RED}[!] Invalid choice{Style.RESET_ALL}")
    
    def test_api_keys(self):
        """Test all API keys"""
        print(f"\n{Fore.YELLOW}[*] Testing API Keys...{Style.RESET_ALL}")
        
        # Test HIBP
        if self.config.HIBP_API_KEY:
            try:
                headers = {'hibp-api-key': self.config.HIBP_API_KEY}
                response = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/test@example.com', 
                                      headers=headers, timeout=5)
                if response.status_code in [200, 404]:
                    print(f"{Fore.GREEN}[✓] HaveIBeenPwned API Key: Working{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}[✗] HaveIBeenPwned API Key: Invalid (Status: {response.status_code}){Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}[✗] HaveIBeenPwned API Key: Error{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] HaveIBeenPwned API Key: Not set{Style.RESET_ALL}")
        
        # Similar tests for other APIs...
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def test_all_services(self):
        """Test all services"""
        print(f"\n{Fore.YELLOW}[*] Testing all services...{Style.RESET_ALL}")
        
        test_email = "test@example.com"
        results = []
        
        for service_name, service_info in self.services.services.items():
            try:
                start = time.time()
                result = service_info["check_method"](test_email)
                elapsed = time.time() - start
                
                if isinstance(result, dict):
                    found = result.get('found', False)
                    confidence = result.get('confidence', 0.0)
                else:
                    found = result
                    confidence = 1.0
                
                results.append({
                    'service': service_name,
                    'time': elapsed,
                    'success': True,
                    'found': found,
                    'confidence': confidence
                })
                
                color = Fore.GREEN if found else Fore.YELLOW
                print(f"  {color}{service_name:20} {elapsed:.2f}s  confidence: {confidence:.1f}{Style.RESET_ALL}")
                
            except Exception as e:
                results.append({
                    'service': service_name,
                    'time': 0,
                    'success': False,
                    'error': str(e)
                })
                print(f"  {Fore.RED}{service_name:20} Error: {e}{Style.RESET_ALL}")
        
        # Summary
        success_count = sum(1 for r in results if r['success'])
        avg_time = sum(r['time'] for r in results if r['success']) / success_count if success_count > 0 else 0
        
        print(f"\n{Fore.CYAN}[*] Test complete: {success_count}/{len(results)} services working, avg time: {avg_time:.2f}s{Style.RESET_ALL}")
    
    def restore_database(self):
        """Restore database from backup"""
        print(f"\n{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          DATABASE RESTORE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'━'*80}{Style.RESET_ALL}")
        
        # List backups
        backups = []
        if os.path.exists(self.config.BACKUP_DIR):
            for file in os.listdir(self.config.BACKUP_DIR):
                if file.endswith('.db.gz'):
                    backups.append(os.path.join(self.config.BACKUP_DIR, file))
        
        if not backups:
            print(f"{Fore.YELLOW}[!] No backups found{Style.RESET_ALL}")
            return
        
        print(f"{Fore.WHITE}Available backups:{Style.RESET_ALL}")
        for idx, backup in enumerate(sorted(backups, reverse=True)[:10], 1):
            size = os.path.getsize(backup) / 1024
            print(f"  {idx}. {os.path.basename(backup)} ({size:.1f} KB)")
        
        choice = input(f"\n{Fore.WHITE}Select backup to restore (1-{min(10, len(backups))}): {Style.RESET_ALL}").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= min(10, len(backups)):
            backup_file = sorted(backups, reverse=True)[int(choice) - 1]
            
            confirm = input(f"\n{Fore.RED}[!] Restore from {os.path.basename(backup_file)}? Current data will be lost! (y/n): {Style.RESET_ALL}").lower()
            
            if confirm == 'y':
                try:
                    # Close current connection
                    self.database.conn.close()
                    
                    # Decompress backup
                    with open(backup_file, 'rb') as f:
                        compressed = f.read()
                    
                    data = zlib.decompress(compressed)
                    
                    # Write to database file
                    with open(self.config.DB_FILE, 'wb') as f:
                        f.write(data)
                    
                    # Reconnect
                    self.database.conn = sqlite3.connect(self.config.DB_FILE, check_same_thread=False)
                    self.database.conn.row_factory = sqlite3.Row
                    
                    print(f"{Fore.GREEN}[✓] Database restored from backup{Style.RESET_ALL}")
                    
                except Exception as e:
                    print(f"{Fore.RED}[!] Restore error: {e}{Style.RESET_ALL}")
                    # Reconnect on error
                    self.database.conn = sqlite3.connect(self.config.DB_FILE, check_same_thread=False)
                    self.database.conn.row_factory = sqlite3.Row
        
        input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
    
    def show_statistics(self):
        """Show detailed statistics"""
        print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📊 DETAILED STATISTICS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        cache_stats = self.cache.get_stats()
        proxy_stats = self.network.proxy_manager.get_proxy_stats()
        db_stats = self.database.get_dashboard_stats()
        
        total_time = time.time() - self.stats['start_time']
        
        print(f"{Fore.WHITE}GENERAL:{Style.RESET_ALL}")
        print(f"  Total Emails Checked: {Fore.CYAN}{self.stats['total_emails']}{Style.RESET_ALL}")
        print(f"  Total Service Checks: {Fore.YELLOW}{self.stats['total_checks']}{Style.RESET_ALL}")
        print(f"  Successful Finds: {Fore.GREEN}{self.stats['successful_checks']}{Style.RESET_ALL}")
        print(f"  Success Rate: {Fore.MAGENTA}{(self.stats['successful_checks']/self.stats['total_checks']*100 if self.stats['total_checks'] > 0 else 0):.1f}%{Style.RESET_ALL}")
        
        print(f"\n{Fore.WHITE}CACHE:{Style.RESET_ALL}")
        print(f"  Hits: {cache_stats['hits']}")
        print(f"  Misses: {cache_stats['misses']}")
        print(f"  Hit Rate: {cache_stats['hit_rate']:.1f}%")
        print(f"  Size: {cache_stats['size']} entries")
        print(f"  Avg Age: {cache_stats['avg_age_hours']:.1f} hours")
        
        print(f"\n{Fore.WHITE}NETWORK:{Style.RESET_ALL}")
        print(f"  Proxies: {proxy_stats['working']} working / {proxy_stats['total']} total")
        print(f"  Requests Made: {self.stats.get('requests_made', 0)}")
        print(f"  Avg Speed: {self.stats['total_checks']/max(total_time, 1):.1f} checks/sec")
        
        print(f"\n{Fore.WHITE}DATABASE:{Style.RESET_ALL}")
        print(f"  Stored Emails: {db_stats.get('total_emails', 0)}")
        print(f"  Checked Today: {db_stats.get('checked_today', 0)}")
        print(f"  Total Found: {db_stats.get('total_found', 0)}")
        print(f"  Services Tracked: {db_stats.get('total_services', 0)}")
        
        print(f"\n{Fore.WHITE}PERFORMANCE:{Style.RESET_ALL}")
        print(f"  Uptime: {timedelta(seconds=int(total_time))}")
        print(f"  Peak Memory: {self.stats['peak_memory']:.1f} MB")
        print(f"  Threads Active: {self.config.MAX_WORKERS}")
        print(f"  Processes: {self.config.MAX_PROCESSES}")
        
        # Service-specific stats
        if db_stats.get('top_services'):
            print(f"\n{Fore.WHITE}TOP 5 SERVICES BY SUCCESS RATE:{Style.RESET_ALL}")
            for service in db_stats['top_services'][:5]:
                print(f"  {service['service_name']:20} - {service['success_rate']:5.1f}% ({service['found']}/{service['total']})")
        
        # Domain stats
        if db_stats.get('top_domains'):
            print(f"\n{Fore.WHITE}TOP 5 DOMAINS:{Style.RESET_ALL}")
            for domain in db_stats['top_domains'][:5]:
                print(f"  {domain['domain']:30} - {domain['count']:6} emails")
    
    def _create_sample_emails_file(self, filename):
        """Create sample emails file"""
        sample_emails = [
            "example@gmail.com",
            "test@yahoo.com",
            "demo@outlook.com",
            "sample@hotmail.com",
            "admin@protonmail.com",
            "user@icloud.com",
            "contact@aol.com",
            "info@mail.com",
            "support@zoho.com",
            "sales@yandex.com"
        ]
        
        with open(filename, 'w') as f:
            f.write("# Sample email list for Mega Email Checker\n")
            f.write("# Add your emails below, one per line\n\n")
            for email in sample_emails:
                f.write(f"{email}\n")
        
        print(f"{Fore.GREEN}[+] Created sample file: {filename}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Add your emails to this file and run again{Style.RESET_ALL}")

# ========== MAIN EXECUTION ==========
def main():
    """Main entry point"""
    try:
        # Create necessary directories
        os.makedirs("backups", exist_ok=True)
        os.makedirs("proxies", exist_ok=True)
        
        # Create necessary files if they don't exist
        if not os.path.exists("proxies.txt"):
            with open("proxies.txt", "w") as f:
                f.write("# Add your proxies here, one per line\n")
                f.write("# Format: protocol://user:pass@ip:port or ip:port\n")
                f.write("# Example:\n")
                f.write("# http://user:pass@123.456.789.0:8080\n")
                f.write("# socks5://127.0.0.1:9050\n")
                f.write("# 123.456.789.0:3128\n")
        
        if not os.path.exists("emails.txt"):
            with open("emails.txt", "w") as f:
                f.write("# Add emails to check here, one per line\n")
                f.write("# Example:\n")
                f.write("example@gmail.com\n")
                f.write("test@yahoo.com\n")
                f.write("demo@outlook.com\n")
        
        if not os.path.exists("disposable_domains.txt"):
            with open("disposable_domains.txt", "w") as f:
                f.write("# List of disposable email domains\n")
                f.write("tempmail.com\n")
                f.write("10minutemail.com\n")
                f.write("mailinator.com\n")
        
        # Initialize and run
        checker = MegaEmailCheckerUltimatePro()
        checker.interactive_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}[*] Program interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Critical error: {e}{Style.RESET_ALL}")
        import traceback
        traceback.print_exc()
    finally:
        print(f"\n{Fore.CYAN}[*] Mega Email Checker Ultra VIP terminated{Style.RESET_ALL}")

if __name__ == "__main__":
    main()