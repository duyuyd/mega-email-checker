#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# MEGA EMAIL CHECKER PRO - LIGHTWEIGHT ADVANCED
# DEVELOPED BY MR DUYKA - TERMUX COMPATIBLE

import requests
import time
import json
import random
import sys
import os
import re
import hashlib
import threading
from datetime import datetime
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor, as_completed

init(autoreset=True)

class AdvancedEmailChecker:
    def __init__(self):
        self.version = "PRO 2.0 LIGHT"
        self.developer = "MR DUYKA"
        self.results_file = "pro_results.txt"
        self.cache_file = "cache.json"
        self.cache = self.load_cache()
        
        # Optimized services for Termux
        self.services = {
            "Facebook": {"emoji": "👤", "color": Fore.BLUE, "priority": 1},
            "Google": {"emoji": "🔍", "color": Fore.RED, "priority": 1},
            "Instagram": {"emoji": "📷", "color": Fore.MAGENTA, "priority": 1},
            "Twitter/X": {"emoji": "🐦", "color": Fore.CYAN, "priority": 2},
            "TikTok": {"emoji": "📱", "color": Fore.BLACK, "priority": 2},
            "Netflix": {"emoji": "🎬", "color": Fore.RED, "priority": 3},
            "PayPal": {"emoji": "💰", "color": Fore.BLUE, "priority": 3},
            "Discord": {"emoji": "🎮", "color": Fore.CYAN, "priority": 3},
            "Microsoft": {"emoji": "🪟", "color": Fore.BLUE, "priority": 3},
            "Amazon": {"emoji": "📦", "color": Fore.YELLOW, "priority": 4},
            "LinkedIn": {"emoji": "💼", "color": Fore.BLUE, "priority": 4},
            "GitHub": {"emoji": "💻", "color": Fore.WHITE, "priority": 4},
            "Spotify": {"emoji": "🎵", "color": Fore.GREEN, "priority": 4},
            "Snapchat": {"emoji": "👻", "color": Fore.YELLOW, "priority": 5},
            "eBay": {"emoji": "🛒", "color": Fore.YELLOW, "priority": 5},
            "Steam": {"emoji": "🎮", "color": Fore.WHITE, "priority": 5},
        }
        
        # Realistic user agents
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0) AppleWebKit/605.1.15',
            'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/120.0 Firefox/120.0',
        ]
        
        # Load proxies if available
        self.proxies = self.load_proxies()
        self.session_pool = {}
        self.checked_count = 0

    def load_cache(self):
        """Load cache from file"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_cache(self):
        """Save cache to file"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass

    def load_proxies(self):
        """Load proxies from file"""
        proxies = []
        if os.path.exists('proxies.txt'):
            try:
                with open('proxies.txt', 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and ':' in line:
                            if not line.startswith('http'):
                                line = f'http://{line}'
                            proxies.append(line)
                print(f"{Fore.GREEN}[+] Loaded {len(proxies)} proxies{Style.RESET_ALL}")
            except:
                pass
        return proxies

    def get_session(self):
        """Get or create session with random proxy"""
        thread_id = threading.get_ident()
        if thread_id not in self.session_pool:
            session = requests.Session()
            
            # Random user agent
            session.headers.update({
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
            })
            
            # Add proxy if available
            if self.proxies:
                proxy = random.choice(self.proxies)
                session.proxies = {'http': proxy, 'https': proxy}
            
            self.session_pool[thread_id] = session
        
        return self.session_pool[thread_id]

    def check_facebook_pro(self, email):
        """Professional Facebook check"""
        cache_key = f"fb_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            # Method 1: Mobile Facebook
            url = 'https://mbasic.facebook.com/login/identify'
            data = {
                'lsd': self._generate_token(8),
                'jazoest': self._generate_token(20, digits=True),
                'email': email,
                'did_submit': 'Search',
            }
            
            response = session.post(url, data=data, timeout=15)
            
            # Check response
            text = response.text.lower()
            
            # Success indicators
            success = ['send code', 'code has been sent', 'we found', 'recover account', 'reset password']
            for indicator in success:
                if indicator in text:
                    self.cache[cache_key] = True
                    return True
            
            # Failure indicators
            failure = ['no search results', 'couldn\'t find', 'not found', 'no account']
            for indicator in failure:
                if indicator in text:
                    self.cache[cache_key] = False
                    return False
            
            # Method 2: Check profile redirect
            try:
                response2 = session.get(
                    f'https://www.facebook.com/{email.replace("@", "%40")}',
                    allow_redirects=False,
                    timeout=10
                )
                if response2.status_code in [200, 302] and 'facebook' in response2.url:
                    self.cache[cache_key] = True
                    return True
            except:
                pass
            
            # Default to False
            self.cache[cache_key] = False
            return False
            
        except Exception as e:
            return False

    def check_google_pro(self, email):
        """Professional Google check"""
        # Gmail always has account
        if email.lower().endswith('@gmail.com'):
            return True
        
        cache_key = f"google_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            username = email.split('@')[0]
            
            # Google username check
            response = session.get(
                f'https://accounts.google.com/_/signup/webusernameavailability',
                params={'username': username},
                timeout=10
            )
            
            if response.status_code == 200:
                if 'NAME_NOT_AVAILABLE' in response.text:
                    self.cache[cache_key] = True
                    return True
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def check_instagram_pro(self, email):
        """Professional Instagram check"""
        cache_key = f"ig_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            # Get CSRF token
            response = session.get('https://www.instagram.com/accounts/password/reset/', timeout=10)
            csrf_match = re.search(r'"csrf_token":"([^"]+)"', response.text)
            csrf_token = csrf_match.group(1) if csrf_match else 'missing'
            
            headers = {
                'X-CSRFToken': csrf_token,
                'X-Instagram-AJAX': '100',
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/password/reset/',
            }
            
            response2 = session.post(
                'https://www.instagram.com/accounts/account_recovery_send_ajax/',
                data={'email_or_username': email},
                headers=headers,
                timeout=10
            )
            
            if response2.status_code == 200:
                result = 'user' in response2.text.lower() or 'email_sent' in response2.text.lower()
                self.cache[cache_key] = result
                return result
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def check_twitter_pro(self, email):
        """Professional Twitter/X check"""
        cache_key = f"tw_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            headers = {
                'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            }
            
            response = session.get(
                'https://api.twitter.com/i/users/email_available.json',
                params={'email': email},
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    result = not data.get('valid', True)
                    self.cache[cache_key] = result
                    return result
                except:
                    pass
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def check_tiktok_pro(self, email):
        """Professional TikTok check"""
        cache_key = f"tt_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            headers = {
                'Content-Type': 'application/json',
                'X-Secsdk-Csrf-Token': '000100000001',
            }
            
            response = session.post(
                'https://www.tiktok.com/api/user/check_email/',
                json={'email': email},
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    result = data.get('data', {}).get('exist', False)
                    self.cache[cache_key] = result
                    return result
                except:
                    pass
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def check_netflix_pro(self, email):
        """Professional Netflix check"""
        cache_key = f"nf_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://www.netflix.com/login',
                data={'userLoginId': email},
                timeout=10
            )
            
            result = 'password' in response.text.lower()
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_paypal_pro(self, email):
        """Professional PayPal check"""
        cache_key = f"pp_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://www.paypal.com/authflow/password-recovery/',
                data={'email': email},
                timeout=10
            )
            
            result = 'recovery' in response.text.lower() or 'reset' in response.text.lower()
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_discord_pro(self, email):
        """Professional Discord check"""
        cache_key = f"dc_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://discord.com/api/v9/auth/register',
                json={
                    'email': email,
                    'username': f'check{random.randint(10000, 99999)}',
                    'password': 'TestPass123!',
                    'date_of_birth': '1990-01-01',
                },
                timeout=10
            )
            
            result = response.status_code == 400 and ('EMAIL_ALREADY_REGISTERED' in response.text or 'email_taken' in response.text.lower())
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_microsoft_pro(self, email):
        """Professional Microsoft check"""
        cache_key = f"ms_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://login.live.com/GetCredentialType.srf',
                json={'Username': email},
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    result = data.get('IfExistsResult') == 0
                    self.cache[cache_key] = result
                    return result
                except:
                    pass
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def check_amazon_pro(self, email):
        """Professional Amazon check"""
        cache_key = f"amz_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://www.amazon.com/ap/signin',
                data={'email': email},
                timeout=10
            )
            
            result = 'password' in response.text.lower() or 'enter your password' in response.text.lower()
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_linkedin_pro(self, email):
        """Professional LinkedIn check"""
        cache_key = f"li_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://www.linkedin.com/uas/request-password-reset',
                data={'userName': email},
                timeout=10
            )
            
            result = 'reset' in response.text.lower() or 'email sent' in response.text.lower()
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_github_pro(self, email):
        """Professional GitHub check"""
        cache_key = f"gh_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://github.com/password_reset',
                data={'email': email},
                timeout=10
            )
            
            result = 'check your email' in response.text.lower() or 'email sent' in response.text.lower()
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_spotify_pro(self, email):
        """Professional Spotify check"""
        cache_key = f"sp_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://www.spotify.com/api/signup/validate',
                json={'email': email},
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    result = data.get('status') == 20
                    self.cache[cache_key] = result
                    return result
                except:
                    pass
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def check_snapchat_pro(self, email):
        """Professional Snapchat check"""
        cache_key = f"sc_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://accounts.snapchat.com/accounts/get_username_suggestions',
                json={'email': email},
                timeout=10
            )
            
            result = response.status_code == 200 and ('taken' in response.text.lower() or 'unavailable' in response.text.lower())
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_ebay_pro(self, email):
        """Professional eBay check"""
        cache_key = f"eb_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://signin.ebay.com/ws/eBayISAPI.dll',
                data={'userid': email},
                timeout=10
            )
            
            result = 'enter your password' in response.text.lower()
            self.cache[cache_key] = result
            return result
            
        except:
            return False

    def check_steam_pro(self, email):
        """Professional Steam check"""
        cache_key = f"st_{hashlib.md5(email.encode()).hexdigest()}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        try:
            session = self.get_session()
            
            response = session.post(
                'https://store.steampowered.com/join/checkavail/',
                data={'email': email},
                timeout=10
            )
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    result = not data.get('bAvailable', True)
                    self.cache[cache_key] = result
                    return result
                except:
                    pass
            
            self.cache[cache_key] = False
            return False
            
        except:
            return False

    def _generate_token(self, length=8, digits=False):
        """Generate random token"""
        if digits:
            chars = '0123456789'
        else:
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choice(chars) for _ in range(length))

    # ========== MAIN CHECK FUNCTION ==========
    
    def check_service(self, service_name, email):
        """Check a service"""
        method_name = f"check_{service_name.lower().replace('/', '_').replace('-', '_')}_pro"
        method = getattr(self, method_name, None)
        
        if method:
            return method(email)
        return False

    def check_single_email_advanced(self, email):
        """Advanced check with threading"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🚀 ADVANCED CHECK: {email}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        start_time = time.time()
        results = {}
        
        # Sort services by priority
        sorted_services = sorted(
            self.services.items(),
            key=lambda x: x[1]["priority"]
        )
        
        # Use ThreadPoolExecutor for parallel checking
        with ThreadPoolExecutor(max_workers=8) as executor:
            future_to_service = {}
            
            for service_name, service_info in sorted_services:
                future = executor.submit(self.check_service, service_name, email)
                future_to_service[future] = (service_name, service_info)
                time.sleep(0.1)  # Stagger requests
            
            # Process results as they complete
            completed = 0
            for future in as_completed(future_to_service):
                service_name, service_info = future_to_service[future]
                emoji = service_info['emoji']
                color = service_info['color']
                
                completed += 1
                try:
                    result = future.result(timeout=15)
                except:
                    result = False
                
                results[service_name] = result
                
                # Display result
                service_display = f"{service_name:12}"
                status = f"{Fore.GREEN}✅ FOUND" if result else f"{Fore.RED}❌ NOT FOUND"
                print(f"[{completed:2d}/{len(self.services)}] {emoji} {color}{service_display}{Style.RESET_ALL} {status}")
        
        elapsed_time = time.time() - start_time
        self.checked_count += 1
        self.save_cache()
        
        return results, elapsed_time

    def display_results(self, email, results, elapsed_time):
        """Display results professionally"""
        print(f"\n{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}          PROFESSIONAL RESULTS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'═'*60}{Style.RESET_ALL}")
        
        print(f"{Fore.WHITE}📧 Email: {Fore.CYAN}{email}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}⏱️  Time: {Fore.YELLOW}{elapsed_time:.1f}s{Style.RESET_ALL}")
        
        # Gmail note
        if email.lower().endswith('@gmail.com'):
            print(f"{Fore.GREEN}📝 Note: Gmail address - Google account exists{Style.RESET_ALL}")
        
        # Group results
        found_services = [s for s, found in results.items() if found]
        
        if found_services:
            print(f"\n{Fore.GREEN}✅ ACCOUNTS FOUND ({len(found_services)}):{Style.RESET_ALL}")
            
            # Categorize
            categories = {
                "Social Media": ["Facebook", "Instagram", "Twitter/X", "LinkedIn", "Snapchat"],
                "Entertainment": ["TikTok", "Netflix", "Spotify"],
                "Financial": ["PayPal", "Amazon", "eBay"],
                "Gaming": ["Discord", "Steam"],
                "Tech": ["Google", "Microsoft", "GitHub"]
            }
            
            for category, services in categories.items():
                cat_services = [s for s in found_services if s in services]
                if cat_services:
                    print(f"\n{Fore.CYAN}   {category}:{Style.RESET_ALL}")
                    for service in cat_services:
                        emoji = self.services[service]['emoji']
                        color = self.services[service]['color']
                        print(f"     {emoji} {color}{service}{Style.RESET_ALL}")
            
            # Statistics
            print(f"\n{Fore.YELLOW}📊 Statistics:{Style.RESET_ALL}")
            print(f"   • Total: {len(found_services)}/{len(self.services)}")
            print(f"   • Cache hits: {self.get_cache_hits(email)}")
            print(f"   • Speed: {elapsed_time/len(self.services):.1f}s per service")
            
        else:
            print(f"\n{Fore.RED}❌ NO ACCOUNTS FOUND{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}⚡ Performance:{Style.RESET_ALL}")
        print(f"   • Threads: 8 parallel")
        print(f"   • Cache: {len(self.cache)} entries")
        print(f"   • Proxies: {len(self.proxies)} available")
        print(f"   • Saved to: {self.results_file}")

    def get_cache_hits(self, email):
        """Get cache hit count"""
        hits = 0
        for service in self.services:
            cache_key = f"{service.lower().split('/')[0]}_{hashlib.md5(email.encode()).hexdigest()}"
            if cache_key in self.cache:
                hits += 1
        return f"{hits}/{len(self.services)}"

    def save_results(self, email, results):
        """Save results to file"""
        try:
            with open(self.results_file, 'a', encoding='utf-8') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found_services = [s for s, found in results.items() if found]
                
                f.write(f"\n{'═'*60}\n")
                f.write(f"📧 Email: {email}\n")
                f.write(f"⏰ Time: {timestamp}\n")
                f.write(f"📊 Found: {len(found_services)}/{len(results)}\n")
                
                if found_services:
                    f.write("✅ Accounts:\n")
                    for service in found_services:
                        emoji = self.services[service]['emoji']
                        f.write(f"   {emoji} {service}\n")
                f.write(f"{'═'*60}\n")
        except Exception as e:
            print(f"{Fore.RED}[!] Error saving: {e}{Style.RESET_ALL}")

    def show_banner(self):
        banner = f"""
{Fore.CYAN}
╔╦╗┬┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┬┌─┐┬┌─┐  ╔═╗┌─┐┬─┐┌─┐┌─┐
 ║ ├┴┐├┤ ├─┤   ║║║├─┤│││├┤ ││ ┬│└─┐  ╠═╝├┤ ├┬┘└─┐├┤ 
 ╩ ┴ ┴└─┘┴ ┴  ═╩╝┴┴ ┴┘└┘└─┘┴└─┘┴└─┘  ╩  └─┘┴└─└─┘└─┘
{Style.RESET_ALL}
{Fore.YELLOW}╔══════════════════════════════════════════════════╗{Style.RESET_ALL}
{Fore.YELLOW}║   MEGA EMAIL CHECKER {self.version}                ║{Style.RESET_ALL}
{Fore.YELLOW}║        DEVELOPED BY {self.developer}                ║{Style.RESET_ALL}
{Fore.YELLOW}╚══════════════════════════════════════════════════╝{Style.RESET_ALL}
{Fore.CYAN}[*] SERVICES     : {len(self.services)} PLATFORMS{Style.RESET_ALL}
{Fore.CYAN}[*] TECHNOLOGY   : THREADED + CACHED + PROXY READY{Style.RESET_ALL}
{Fore.GREEN}[*] SPEED        : 8 PARALLEL THREADS{Style.RESET_ALL}
{Fore.YELLOW}[*] CACHE       : {len(self.cache)} ENTRIES{Style.RESET_ALL}
{Fore.RED}[*] TERMUX       : FULLY COMPATIBLE{Style.RESET_ALL}
"""
        print(banner)

    def run(self):
        """Main program"""
        self.show_banner()
        
        while True:
            try:
                print(f"\n{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}          PROFESSIONAL CHECKER{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                print(f"{Fore.WHITE}[1] {Fore.GREEN}Check Single Email{Style.RESET_ALL}")
                print(f"{Fore.WHITE}[2] {Fore.BLUE}Check Multiple Emails{Style.RESET_ALL}")
                print(f"{Fore.WHITE}[3] {Fore.YELLOW}View Results{Style.RESET_ALL}")
                print(f"{Fore.WHITE}[4] {Fore.MAGENTA}Clear Cache{Style.RESET_ALL}")
                print(f"{Fore.WHITE}[5] {Fore.RED}Exit{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'═'*50}{Style.RESET_ALL}")
                
                choice = input(f"\n{Fore.WHITE}Select option (1-5): {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    email = input(f"{Fore.WHITE}Enter email: {Style.RESET_ALL}").strip()
                    if email and '@' in email:
                        results, elapsed = self.check_single_email_advanced(email)
                        self.display_results(email, results, elapsed)
                        self.save_results(email, results)
                    else:
                        print(f"{Fore.RED}[!] Invalid email!{Style.RESET_ALL}")
                    input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
                
                elif choice == '2':
                    print(f"\n{Fore.CYAN}[*] Enter emails (comma separated){Style.RESET_ALL}")
                    emails_input = input(f"{Fore.WHITE}Emails: {Style.RESET_ALL}").strip()
                    emails = [e.strip() for e in emails_input.split(',') if '@' in e.strip()]
                    
                    if emails:
                        for idx, email in enumerate(emails, 1):
                            print(f"\n{Fore.YELLOW}[{idx}/{len(emails)}] Checking: {email}{Style.RESET_ALL}")
                            results, elapsed = self.check_single_email_advanced(email)
                            self.save_results(email, results)
                            
                            if idx < len(emails):
                                wait = 3
                                print(f"{Fore.CYAN}[*] Waiting {wait}s...{Style.RESET_ALL}")
                                time.sleep(wait)
                    else:
                        print(f"{Fore.RED}[!] No valid emails!{Style.RESET_ALL}")
                    input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
                
                elif choice == '3':
                    if os.path.exists(self.results_file):
                        with open(self.results_file, 'r') as f:
                            content = f.read()
                            if content:
                                print(f"\n{Fore.CYAN}{content}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}[!] No results yet{Style.RESET_ALL}")
                    input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
                
                elif choice == '4':
                    self.cache = {}
                    self.save_cache()
                    print(f"{Fore.GREEN}[✓] Cache cleared!{Style.RESET_ALL}")
                    input(f"\n{Fore.YELLOW}[*] Press Enter...{Style.RESET_ALL}")
                
                elif choice == '5':
                    print(f"\n{Fore.GREEN}[*] Thank you for using Professional Checker!{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}[*] Total checks: {self.checked_count}{Style.RESET_ALL}")
                    self.save_cache()
                    break
                
                else:
                    print(f"{Fore.RED}[!] Invalid choice!{Style.RESET_ALL}")
            
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}[*] Exiting...{Style.RESET_ALL}")
                self.save_cache()
                break
            except Exception as e:
                print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.YELLOW}[*] Starting Mega Email Checker PRO...{Style.RESET_ALL}")
    time.sleep(1)
    
    checker = AdvancedEmailChecker()
    checker.run()

if __name__ == "__main__":
    main()
