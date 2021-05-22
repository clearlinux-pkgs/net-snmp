#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF07B9D2DACB19FD6 (net-snmp-admins@lists.sourceforge.net)
#
Name     : net-snmp
Version  : 5.9
Release  : 46
URL      : https://sourceforge.net/projects/net-snmp/files/net-snmp/5.9/net-snmp-5.9.tar.gz
Source0  : https://sourceforge.net/projects/net-snmp/files/net-snmp/5.9/net-snmp-5.9.tar.gz
Source1  : snmpd.service
Source2  : snmptrapd.service
Source3  : https://sourceforge.net/projects/net-snmp/files/net-snmp/5.9/net-snmp-5.9.tar.gz.asc
Summary  : unknown
Group    : Development/Tools
License  : BSD-3-Clause OpenSSL
Requires: net-snmp-bin = %{version}-%{release}
Requires: net-snmp-data = %{version}-%{release}
Requires: net-snmp-lib = %{version}-%{release}
Requires: net-snmp-license = %{version}-%{release}
Requires: net-snmp-man = %{version}-%{release}
Requires: net-snmp-perl = %{version}-%{release}
Requires: net-snmp-services = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : e2fsprogs-dev
BuildRequires : libpcap-dev
BuildRequires : ncurses-dev
BuildRequires : net-tools
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : perl(NetSNMP::OID)
BuildRequires : pkgconfig(libpci)
BuildRequires : pkgconfig(ncurses)
BuildRequires : procps-ng
BuildRequires : valgrind
BuildRequires : valgrind-dev
Patch1: cve-2014-2285.nopatch
Patch2: 0001-Use-vendor-path.patch

%description
Net-SNMP provides tools and libraries relating to the Simple Network
Management Protocol including: An extensible agent, An SNMP library,
tools to request or set information from SNMP agents, tools to
generate and handle SNMP traps, etc.  Using SNMP you can check the
status of a network of computers, routers, switches, servers, ... to
evaluate the state of your network.

%package bin
Summary: bin components for the net-snmp package.
Group: Binaries
Requires: net-snmp-data = %{version}-%{release}
Requires: net-snmp-license = %{version}-%{release}
Requires: net-snmp-services = %{version}-%{release}

%description bin
bin components for the net-snmp package.


%package data
Summary: data components for the net-snmp package.
Group: Data

%description data
data components for the net-snmp package.


%package dev
Summary: dev components for the net-snmp package.
Group: Development
Requires: net-snmp-lib = %{version}-%{release}
Requires: net-snmp-bin = %{version}-%{release}
Requires: net-snmp-data = %{version}-%{release}
Provides: net-snmp-devel = %{version}-%{release}
Requires: net-snmp = %{version}-%{release}

%description dev
dev components for the net-snmp package.


%package lib
Summary: lib components for the net-snmp package.
Group: Libraries
Requires: net-snmp-data = %{version}-%{release}
Requires: net-snmp-license = %{version}-%{release}

%description lib
lib components for the net-snmp package.


%package license
Summary: license components for the net-snmp package.
Group: Default

%description license
license components for the net-snmp package.


%package man
Summary: man components for the net-snmp package.
Group: Default

%description man
man components for the net-snmp package.


%package perl
Summary: perl components for the net-snmp package.
Group: Default
Requires: net-snmp = %{version}-%{release}

%description perl
perl components for the net-snmp package.


%package services
Summary: services components for the net-snmp package.
Group: Systemd services

%description services
services components for the net-snmp package.


%prep
%setup -q -n net-snmp-5.9
cd %{_builddir}/net-snmp-5.9
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597771053
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --disable-des
## make_prepend content
rm perl/Makefile
## make_prepend end
make  %{?_smp_mflags}  -j1

%install
export SOURCE_DATE_EPOCH=1597771053
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/net-snmp
cp %{_builddir}/net-snmp-5.9/COPYING %{buildroot}/usr/share/package-licenses/net-snmp/3783c8f99c31700ddd8453682f0178c88c14012c
cp %{_builddir}/net-snmp-5.9/python/LICENSE %{buildroot}/usr/share/package-licenses/net-snmp/77bac2446a3e00a3aa1b8aaba3506d4ea46d6e5d
cp %{_builddir}/net-snmp-5.9/snmplib/openssl/OPENSSL-LICENSE %{buildroot}/usr/share/package-licenses/net-snmp/c9c50bd46b69aba62e61c65d8ab08dd1e8c83b38
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/snmpd.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/snmptrapd.service
## install_append content
find %{buildroot} -type f -name '*.a' -exec rm -f {} \;
find %{buildroot} -type f -name 'perllocal.pod' -exec rm -f {} \;
find %{buildroot} -type f -name '.packlist' -exec rm -f {} \;
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/agentxtrap
/usr/bin/checkbandwidth
/usr/bin/encode_keychange
/usr/bin/fixproc
/usr/bin/ipf-mod.pl
/usr/bin/mib2c
/usr/bin/mib2c-update
/usr/bin/net-snmp-cert
/usr/bin/net-snmp-config
/usr/bin/net-snmp-create-v3-user
/usr/bin/snmp-bridge-mib
/usr/bin/snmpbulkget
/usr/bin/snmpbulkwalk
/usr/bin/snmpcheck
/usr/bin/snmpconf
/usr/bin/snmpd
/usr/bin/snmpdelta
/usr/bin/snmpdf
/usr/bin/snmpget
/usr/bin/snmpgetnext
/usr/bin/snmpinform
/usr/bin/snmpnetstat
/usr/bin/snmppcap
/usr/bin/snmpping
/usr/bin/snmpps
/usr/bin/snmpset
/usr/bin/snmpstatus
/usr/bin/snmptable
/usr/bin/snmptest
/usr/bin/snmptop
/usr/bin/snmptranslate
/usr/bin/snmptrap
/usr/bin/snmptrapd
/usr/bin/snmpusm
/usr/bin/snmpvacm
/usr/bin/snmpwalk
/usr/bin/tkmib
/usr/bin/traptoemail

%files data
%defattr(-,root,root,-)
/usr/share/snmp/mib2c-data/default-mfd-top.m2c
/usr/share/snmp/mib2c-data/details-enums.m2i
/usr/share/snmp/mib2c-data/details-node.m2i
/usr/share/snmp/mib2c-data/details-table.m2i
/usr/share/snmp/mib2c-data/generic-ctx-copy.m2i
/usr/share/snmp/mib2c-data/generic-ctx-get.m2i
/usr/share/snmp/mib2c-data/generic-ctx-set.m2i
/usr/share/snmp/mib2c-data/generic-data-allocate.m2i
/usr/share/snmp/mib2c-data/generic-data-context.m2i
/usr/share/snmp/mib2c-data/generic-get-U64.m2i
/usr/share/snmp/mib2c-data/generic-get-char.m2i
/usr/share/snmp/mib2c-data/generic-get-decl-bot.m2i
/usr/share/snmp/mib2c-data/generic-get-decl.m2i
/usr/share/snmp/mib2c-data/generic-get-long.m2i
/usr/share/snmp/mib2c-data/generic-get-oid.m2i
/usr/share/snmp/mib2c-data/generic-header-bottom.m2i
/usr/share/snmp/mib2c-data/generic-header-top.m2i
/usr/share/snmp/mib2c-data/generic-source-includes.m2i
/usr/share/snmp/mib2c-data/generic-table-constants.m2c
/usr/share/snmp/mib2c-data/generic-table-enums.m2c
/usr/share/snmp/mib2c-data/generic-table-indexes-from-oid.m2i
/usr/share/snmp/mib2c-data/generic-table-indexes-set.m2i
/usr/share/snmp/mib2c-data/generic-table-indexes-to-oid.m2i
/usr/share/snmp/mib2c-data/generic-table-indexes-varbind-setup.m2i
/usr/share/snmp/mib2c-data/generic-table-indexes.m2i
/usr/share/snmp/mib2c-data/generic-table-oids.m2c
/usr/share/snmp/mib2c-data/generic-value-map-func.m2i
/usr/share/snmp/mib2c-data/generic-value-map-reverse.m2i
/usr/share/snmp/mib2c-data/generic-value-map.m2i
/usr/share/snmp/mib2c-data/m2c-internal-warning.m2i
/usr/share/snmp/mib2c-data/m2c_setup_enum.m2i
/usr/share/snmp/mib2c-data/m2c_setup_node.m2i
/usr/share/snmp/mib2c-data/m2c_setup_table.m2i
/usr/share/snmp/mib2c-data/m2c_table_save_defaults.m2i
/usr/share/snmp/mib2c-data/mfd-access-container-cached-defines.m2i
/usr/share/snmp/mib2c-data/mfd-access-unsorted-external-defines.m2i
/usr/share/snmp/mib2c-data/mfd-data-access.m2c
/usr/share/snmp/mib2c-data/mfd-data-get.m2c
/usr/share/snmp/mib2c-data/mfd-data-set.m2c
/usr/share/snmp/mib2c-data/mfd-doxygen.m2c
/usr/share/snmp/mib2c-data/mfd-interactive-setup.m2c
/usr/share/snmp/mib2c-data/mfd-interface.m2c
/usr/share/snmp/mib2c-data/mfd-makefile.m2m
/usr/share/snmp/mib2c-data/mfd-persistence.m2i
/usr/share/snmp/mib2c-data/mfd-readme.m2c
/usr/share/snmp/mib2c-data/mfd-top.m2c
/usr/share/snmp/mib2c-data/node-get.m2i
/usr/share/snmp/mib2c-data/node-set.m2i
/usr/share/snmp/mib2c-data/node-storage.m2i
/usr/share/snmp/mib2c-data/node-validate.m2i
/usr/share/snmp/mib2c-data/node-varbind-validate.m2i
/usr/share/snmp/mib2c-data/parent-dependencies.m2i
/usr/share/snmp/mib2c-data/parent-set.m2i
/usr/share/snmp/mib2c-data/subagent.m2c
/usr/share/snmp/mib2c-data/syntax-COUNTER64-get.m2i
/usr/share/snmp/mib2c-data/syntax-DateAndTime-get.m2d
/usr/share/snmp/mib2c-data/syntax-DateAndTime-get.m2i
/usr/share/snmp/mib2c-data/syntax-DateAndTime-readme.m2i
/usr/share/snmp/mib2c-data/syntax-InetAddress-get.m2i
/usr/share/snmp/mib2c-data/syntax-InetAddress-set.m2i
/usr/share/snmp/mib2c-data/syntax-InetAddressType-get.m2i
/usr/share/snmp/mib2c-data/syntax-InetAddressType-set.m2i
/usr/share/snmp/mib2c-data/syntax-RowStatus-dependencies.m2i
/usr/share/snmp/mib2c-data/syntax-RowStatus-get.m2i
/usr/share/snmp/mib2c-data/syntax-RowStatus-varbind-validate.m2i
/usr/share/snmp/mib2c-data/syntax-StorageType-dependencies.m2i
/usr/share/snmp/mib2c-data/syntax-TestAndIncr-get.m2i
/usr/share/snmp/mib2c.access_functions.conf
/usr/share/snmp/mib2c.array-user.conf
/usr/share/snmp/mib2c.check_values.conf
/usr/share/snmp/mib2c.check_values_local.conf
/usr/share/snmp/mib2c.column_defines.conf
/usr/share/snmp/mib2c.column_enums.conf
/usr/share/snmp/mib2c.column_storage.conf
/usr/share/snmp/mib2c.conf
/usr/share/snmp/mib2c.container.conf
/usr/share/snmp/mib2c.create-dataset.conf
/usr/share/snmp/mib2c.genhtml.conf
/usr/share/snmp/mib2c.int_watch.conf
/usr/share/snmp/mib2c.iterate.conf
/usr/share/snmp/mib2c.iterate_access.conf
/usr/share/snmp/mib2c.mfd.conf
/usr/share/snmp/mib2c.notify.conf
/usr/share/snmp/mib2c.old-api.conf
/usr/share/snmp/mib2c.org-mode.conf
/usr/share/snmp/mib2c.perl.conf
/usr/share/snmp/mib2c.raw-table.conf
/usr/share/snmp/mib2c.scalar.conf
/usr/share/snmp/mib2c.table_data.conf
/usr/share/snmp/mibs/AGENTX-MIB.txt
/usr/share/snmp/mibs/BRIDGE-MIB.txt
/usr/share/snmp/mibs/DISMAN-EVENT-MIB.txt
/usr/share/snmp/mibs/DISMAN-SCHEDULE-MIB.txt
/usr/share/snmp/mibs/DISMAN-SCRIPT-MIB.txt
/usr/share/snmp/mibs/EtherLike-MIB.txt
/usr/share/snmp/mibs/HCNUM-TC.txt
/usr/share/snmp/mibs/HOST-RESOURCES-MIB.txt
/usr/share/snmp/mibs/HOST-RESOURCES-TYPES.txt
/usr/share/snmp/mibs/IANA-ADDRESS-FAMILY-NUMBERS-MIB.txt
/usr/share/snmp/mibs/IANA-LANGUAGE-MIB.txt
/usr/share/snmp/mibs/IANA-RTPROTO-MIB.txt
/usr/share/snmp/mibs/IANAifType-MIB.txt
/usr/share/snmp/mibs/IF-INVERTED-STACK-MIB.txt
/usr/share/snmp/mibs/IF-MIB.txt
/usr/share/snmp/mibs/INET-ADDRESS-MIB.txt
/usr/share/snmp/mibs/IP-FORWARD-MIB.txt
/usr/share/snmp/mibs/IP-MIB.txt
/usr/share/snmp/mibs/IPV6-FLOW-LABEL-MIB.txt
/usr/share/snmp/mibs/IPV6-ICMP-MIB.txt
/usr/share/snmp/mibs/IPV6-MIB.txt
/usr/share/snmp/mibs/IPV6-TC.txt
/usr/share/snmp/mibs/IPV6-TCP-MIB.txt
/usr/share/snmp/mibs/IPV6-UDP-MIB.txt
/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
/usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
/usr/share/snmp/mibs/NET-SNMP-MIB.txt
/usr/share/snmp/mibs/NET-SNMP-PASS-MIB.txt
/usr/share/snmp/mibs/NET-SNMP-TC.txt
/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
/usr/share/snmp/mibs/NOTIFICATION-LOG-MIB.txt
/usr/share/snmp/mibs/RFC-1215.txt
/usr/share/snmp/mibs/RFC1155-SMI.txt
/usr/share/snmp/mibs/RFC1213-MIB.txt
/usr/share/snmp/mibs/RMON-MIB.txt
/usr/share/snmp/mibs/SCTP-MIB.txt
/usr/share/snmp/mibs/SMUX-MIB.txt
/usr/share/snmp/mibs/SNMP-COMMUNITY-MIB.txt
/usr/share/snmp/mibs/SNMP-FRAMEWORK-MIB.txt
/usr/share/snmp/mibs/SNMP-MPD-MIB.txt
/usr/share/snmp/mibs/SNMP-NOTIFICATION-MIB.txt
/usr/share/snmp/mibs/SNMP-PROXY-MIB.txt
/usr/share/snmp/mibs/SNMP-TARGET-MIB.txt
/usr/share/snmp/mibs/SNMP-TLS-TM-MIB.txt
/usr/share/snmp/mibs/SNMP-TSM-MIB.txt
/usr/share/snmp/mibs/SNMP-USER-BASED-SM-MIB.txt
/usr/share/snmp/mibs/SNMP-USM-AES-MIB.txt
/usr/share/snmp/mibs/SNMP-USM-DH-OBJECTS-MIB.txt
/usr/share/snmp/mibs/SNMP-USM-HMAC-SHA2-MIB.txt
/usr/share/snmp/mibs/SNMP-VIEW-BASED-ACM-MIB.txt
/usr/share/snmp/mibs/SNMPv2-CONF.txt
/usr/share/snmp/mibs/SNMPv2-MIB.txt
/usr/share/snmp/mibs/SNMPv2-SMI.txt
/usr/share/snmp/mibs/SNMPv2-TC.txt
/usr/share/snmp/mibs/SNMPv2-TM.txt
/usr/share/snmp/mibs/TCP-MIB.txt
/usr/share/snmp/mibs/TRANSPORT-ADDRESS-MIB.txt
/usr/share/snmp/mibs/TUNNEL-MIB.txt
/usr/share/snmp/mibs/UCD-DEMO-MIB.txt
/usr/share/snmp/mibs/UCD-DISKIO-MIB.txt
/usr/share/snmp/mibs/UCD-DLMOD-MIB.txt
/usr/share/snmp/mibs/UCD-IPFWACC-MIB.txt
/usr/share/snmp/mibs/UCD-SNMP-MIB.txt
/usr/share/snmp/mibs/UDP-MIB.txt
/usr/share/snmp/snmp_perl.pl
/usr/share/snmp/snmp_perl_trapd.pl
/usr/share/snmp/snmpconf-data/snmp-data/authopts
/usr/share/snmp/snmpconf-data/snmp-data/debugging
/usr/share/snmp/snmpconf-data/snmp-data/mibs
/usr/share/snmp/snmpconf-data/snmp-data/output
/usr/share/snmp/snmpconf-data/snmp-data/snmpconf-config
/usr/share/snmp/snmpconf-data/snmpd-data/acl
/usr/share/snmp/snmpconf-data/snmpd-data/basic_setup
/usr/share/snmp/snmpconf-data/snmpd-data/extending
/usr/share/snmp/snmpconf-data/snmpd-data/monitor
/usr/share/snmp/snmpconf-data/snmpd-data/operation
/usr/share/snmp/snmpconf-data/snmpd-data/snmpconf-config
/usr/share/snmp/snmpconf-data/snmpd-data/system
/usr/share/snmp/snmpconf-data/snmpd-data/trapsinks
/usr/share/snmp/snmpconf-data/snmptrapd-data/authentication
/usr/share/snmp/snmpconf-data/snmptrapd-data/formatting
/usr/share/snmp/snmpconf-data/snmptrapd-data/logging
/usr/share/snmp/snmpconf-data/snmptrapd-data/runtime
/usr/share/snmp/snmpconf-data/snmptrapd-data/snmpconf-config
/usr/share/snmp/snmpconf-data/snmptrapd-data/traphandle

%files dev
%defattr(-,root,root,-)
/usr/include/net-snmp/agent/agent_callbacks.h
/usr/include/net-snmp/agent/agent_handler.h
/usr/include/net-snmp/agent/agent_index.h
/usr/include/net-snmp/agent/agent_module_config.h
/usr/include/net-snmp/agent/agent_read_config.h
/usr/include/net-snmp/agent/agent_registry.h
/usr/include/net-snmp/agent/agent_sysORTable.h
/usr/include/net-snmp/agent/agent_trap.h
/usr/include/net-snmp/agent/all_helpers.h
/usr/include/net-snmp/agent/auto_nlist.h
/usr/include/net-snmp/agent/baby_steps.h
/usr/include/net-snmp/agent/bulk_to_next.h
/usr/include/net-snmp/agent/cache_handler.h
/usr/include/net-snmp/agent/debug_handler.h
/usr/include/net-snmp/agent/ds_agent.h
/usr/include/net-snmp/agent/instance.h
/usr/include/net-snmp/agent/mfd.h
/usr/include/net-snmp/agent/mib_module_config.h
/usr/include/net-snmp/agent/mib_module_includes.h
/usr/include/net-snmp/agent/mib_modules.h
/usr/include/net-snmp/agent/mode_end_call.h
/usr/include/net-snmp/agent/multiplexer.h
/usr/include/net-snmp/agent/net-snmp-agent-includes.h
/usr/include/net-snmp/agent/netsnmp_close_fds.h
/usr/include/net-snmp/agent/null.h
/usr/include/net-snmp/agent/old_api.h
/usr/include/net-snmp/agent/read_only.h
/usr/include/net-snmp/agent/row_merge.h
/usr/include/net-snmp/agent/scalar.h
/usr/include/net-snmp/agent/scalar_group.h
/usr/include/net-snmp/agent/serialize.h
/usr/include/net-snmp/agent/set_helper.h
/usr/include/net-snmp/agent/snmp_agent.h
/usr/include/net-snmp/agent/snmp_get_statistic.h
/usr/include/net-snmp/agent/snmp_vars.h
/usr/include/net-snmp/agent/stash_cache.h
/usr/include/net-snmp/agent/stash_to_next.h
/usr/include/net-snmp/agent/struct.h
/usr/include/net-snmp/agent/sysORTable.h
/usr/include/net-snmp/agent/table.h
/usr/include/net-snmp/agent/table_array.h
/usr/include/net-snmp/agent/table_container.h
/usr/include/net-snmp/agent/table_data.h
/usr/include/net-snmp/agent/table_dataset.h
/usr/include/net-snmp/agent/table_iterator.h
/usr/include/net-snmp/agent/table_tdata.h
/usr/include/net-snmp/agent/util_funcs.h
/usr/include/net-snmp/agent/util_funcs/MIB_STATS_CACHE_TIMEOUT.h
/usr/include/net-snmp/agent/util_funcs/header_generic.h
/usr/include/net-snmp/agent/util_funcs/header_simple_table.h
/usr/include/net-snmp/agent/var_struct.h
/usr/include/net-snmp/agent/watcher.h
/usr/include/net-snmp/config_api.h
/usr/include/net-snmp/definitions.h
/usr/include/net-snmp/library/README
/usr/include/net-snmp/library/asn1.h
/usr/include/net-snmp/library/callback.h
/usr/include/net-snmp/library/cert_util.h
/usr/include/net-snmp/library/check_varbind.h
/usr/include/net-snmp/library/container.h
/usr/include/net-snmp/library/container_binary_array.h
/usr/include/net-snmp/library/container_iterator.h
/usr/include/net-snmp/library/container_list_ssll.h
/usr/include/net-snmp/library/container_null.h
/usr/include/net-snmp/library/data_list.h
/usr/include/net-snmp/library/default_store.h
/usr/include/net-snmp/library/dir_utils.h
/usr/include/net-snmp/library/factory.h
/usr/include/net-snmp/library/fd_event_manager.h
/usr/include/net-snmp/library/file_utils.h
/usr/include/net-snmp/library/getopt.h
/usr/include/net-snmp/library/int64.h
/usr/include/net-snmp/library/keytools.h
/usr/include/net-snmp/library/large_fd_set.h
/usr/include/net-snmp/library/lcd_time.h
/usr/include/net-snmp/library/md5.h
/usr/include/net-snmp/library/mib.h
/usr/include/net-snmp/library/mt_support.h
/usr/include/net-snmp/library/netsnmp-attribute-format.h
/usr/include/net-snmp/library/oid.h
/usr/include/net-snmp/library/oid_stash.h
/usr/include/net-snmp/library/parse.h
/usr/include/net-snmp/library/read_config.h
/usr/include/net-snmp/library/scapi.h
/usr/include/net-snmp/library/snmp-tc.h
/usr/include/net-snmp/library/snmp.h
/usr/include/net-snmp/library/snmpAliasDomain.h
/usr/include/net-snmp/library/snmpCallbackDomain.h
/usr/include/net-snmp/library/snmpIPBaseDomain.h
/usr/include/net-snmp/library/snmpIPv4BaseDomain.h
/usr/include/net-snmp/library/snmpIPv6BaseDomain.h
/usr/include/net-snmp/library/snmpSocketBaseDomain.h
/usr/include/net-snmp/library/snmpTCPBaseDomain.h
/usr/include/net-snmp/library/snmpTCPDomain.h
/usr/include/net-snmp/library/snmpTCPIPv6Domain.h
/usr/include/net-snmp/library/snmpUDPBaseDomain.h
/usr/include/net-snmp/library/snmpUDPDomain.h
/usr/include/net-snmp/library/snmpUDPIPv4BaseDomain.h
/usr/include/net-snmp/library/snmpUDPIPv6Domain.h
/usr/include/net-snmp/library/snmpUnixDomain.h
/usr/include/net-snmp/library/snmp_alarm.h
/usr/include/net-snmp/library/snmp_api.h
/usr/include/net-snmp/library/snmp_assert.h
/usr/include/net-snmp/library/snmp_client.h
/usr/include/net-snmp/library/snmp_debug.h
/usr/include/net-snmp/library/snmp_enum.h
/usr/include/net-snmp/library/snmp_impl.h
/usr/include/net-snmp/library/snmp_logging.h
/usr/include/net-snmp/library/snmp_parse_args.h
/usr/include/net-snmp/library/snmp_secmod.h
/usr/include/net-snmp/library/snmp_service.h
/usr/include/net-snmp/library/snmp_transport.h
/usr/include/net-snmp/library/snmpusm.h
/usr/include/net-snmp/library/snmpv3-security-includes.h
/usr/include/net-snmp/library/snmpv3.h
/usr/include/net-snmp/library/system.h
/usr/include/net-snmp/library/text_utils.h
/usr/include/net-snmp/library/tools.h
/usr/include/net-snmp/library/transform_oids.h
/usr/include/net-snmp/library/types.h
/usr/include/net-snmp/library/ucd_compat.h
/usr/include/net-snmp/library/vacm.h
/usr/include/net-snmp/library/winpipe.h
/usr/include/net-snmp/library/winservice.h
/usr/include/net-snmp/machine/generic.h
/usr/include/net-snmp/mib_api.h
/usr/include/net-snmp/net-snmp-config.h
/usr/include/net-snmp/net-snmp-features.h
/usr/include/net-snmp/net-snmp-includes.h
/usr/include/net-snmp/output_api.h
/usr/include/net-snmp/pdu_api.h
/usr/include/net-snmp/session_api.h
/usr/include/net-snmp/snmpv3_api.h
/usr/include/net-snmp/system/aix.h
/usr/include/net-snmp/system/bsd.h
/usr/include/net-snmp/system/bsdi.h
/usr/include/net-snmp/system/bsdi3.h
/usr/include/net-snmp/system/bsdi4.h
/usr/include/net-snmp/system/cygwin.h
/usr/include/net-snmp/system/darwin.h
/usr/include/net-snmp/system/dragonfly.h
/usr/include/net-snmp/system/dynix.h
/usr/include/net-snmp/system/freebsd.h
/usr/include/net-snmp/system/freebsd10.h
/usr/include/net-snmp/system/freebsd11.h
/usr/include/net-snmp/system/freebsd12.h
/usr/include/net-snmp/system/freebsd13.h
/usr/include/net-snmp/system/freebsd14.h
/usr/include/net-snmp/system/freebsd2.h
/usr/include/net-snmp/system/freebsd3.h
/usr/include/net-snmp/system/freebsd4.h
/usr/include/net-snmp/system/freebsd5.h
/usr/include/net-snmp/system/freebsd6.h
/usr/include/net-snmp/system/freebsd7.h
/usr/include/net-snmp/system/freebsd8.h
/usr/include/net-snmp/system/freebsd9.h
/usr/include/net-snmp/system/generic.h
/usr/include/net-snmp/system/hpux.h
/usr/include/net-snmp/system/irix.h
/usr/include/net-snmp/system/linux.h
/usr/include/net-snmp/system/mingw32.h
/usr/include/net-snmp/system/mingw32msvc.h
/usr/include/net-snmp/system/mips.h
/usr/include/net-snmp/system/netbsd.h
/usr/include/net-snmp/system/nto-qnx6.h
/usr/include/net-snmp/system/openbsd.h
/usr/include/net-snmp/system/openbsd4.h
/usr/include/net-snmp/system/openbsd5.h
/usr/include/net-snmp/system/openbsd6.h
/usr/include/net-snmp/system/osf5.h
/usr/include/net-snmp/system/solaris.h
/usr/include/net-snmp/system/solaris2.3.h
/usr/include/net-snmp/system/solaris2.4.h
/usr/include/net-snmp/system/solaris2.5.h
/usr/include/net-snmp/system/solaris2.6.h
/usr/include/net-snmp/system/sunos.h
/usr/include/net-snmp/system/svr5.h
/usr/include/net-snmp/system/sysv.h
/usr/include/net-snmp/system/ultrix4.h
/usr/include/net-snmp/types.h
/usr/include/net-snmp/utilities.h
/usr/include/net-snmp/varbind_api.h
/usr/include/net-snmp/version.h
/usr/lib64/libnetsnmp.so
/usr/lib64/libnetsnmpagent.so
/usr/lib64/libnetsnmphelpers.so
/usr/lib64/libnetsnmpmibs.so
/usr/lib64/libnetsnmptrapd.so
/usr/lib64/pkgconfig/netsnmp-agent.pc
/usr/lib64/pkgconfig/netsnmp.pc
/usr/share/man/man3/NetSNMP::ASN.3
/usr/share/man/man3/NetSNMP::ASN.3pm
/usr/share/man/man3/NetSNMP::OID.3
/usr/share/man/man3/NetSNMP::OID.3pm
/usr/share/man/man3/NetSNMP::TrapReceiver.3
/usr/share/man/man3/NetSNMP::TrapReceiver.3pm
/usr/share/man/man3/NetSNMP::agent.3
/usr/share/man/man3/NetSNMP::agent.3pm
/usr/share/man/man3/NetSNMP::agent::default_store.3
/usr/share/man/man3/NetSNMP::agent::default_store.3pm
/usr/share/man/man3/NetSNMP::default_store.3
/usr/share/man/man3/NetSNMP::default_store.3pm
/usr/share/man/man3/NetSNMP::netsnmp_request_infoPtr.3
/usr/share/man/man3/NetSNMP::netsnmp_request_infoPtr.3pm
/usr/share/man/man3/SNMP.3
/usr/share/man/man3/add_mibdir.3
/usr/share/man/man3/add_module_replacement.3
/usr/share/man/man3/config_perror.3
/usr/share/man/man3/config_pwarn.3
/usr/share/man/man3/default_store.3
/usr/share/man/man3/fprint_description.3
/usr/share/man/man3/fprint_objid.3
/usr/share/man/man3/fprint_value.3
/usr/share/man/man3/fprint_variable.3
/usr/share/man/man3/get_module_node.3
/usr/share/man/man3/netsnmp_agent_api.3
/usr/share/man/man3/netsnmp_config_api.3
/usr/share/man/man3/netsnmp_init_mib.3
/usr/share/man/man3/netsnmp_mib_api.3
/usr/share/man/man3/netsnmp_pdu_api.3
/usr/share/man/man3/netsnmp_read_module.3
/usr/share/man/man3/netsnmp_sess_api.3
/usr/share/man/man3/netsnmp_session_api.3
/usr/share/man/man3/netsnmp_trap_api.3
/usr/share/man/man3/netsnmp_varbind_api.3
/usr/share/man/man3/print_description.3
/usr/share/man/man3/print_mib.3
/usr/share/man/man3/print_objid.3
/usr/share/man/man3/print_value.3
/usr/share/man/man3/print_variable.3
/usr/share/man/man3/read_all_mibs.3
/usr/share/man/man3/read_config_print_usage.3
/usr/share/man/man3/read_configs.3
/usr/share/man/man3/read_mib.3
/usr/share/man/man3/read_objid.3
/usr/share/man/man3/read_premib_configs.3
/usr/share/man/man3/register_app_config_handler.3
/usr/share/man/man3/register_app_prenetsnmp_mib_handler.3
/usr/share/man/man3/register_config_handler.3
/usr/share/man/man3/register_const_config_handler.3
/usr/share/man/man3/register_mib_handlers.3
/usr/share/man/man3/register_prenetsnmp_mib_handler.3
/usr/share/man/man3/send_easy_trap.3
/usr/share/man/man3/send_trap_vars.3
/usr/share/man/man3/send_v2trap.3
/usr/share/man/man3/shutdown_mib.3
/usr/share/man/man3/snmp_add_null_var.3
/usr/share/man/man3/snmp_alarm.3
/usr/share/man/man3/snmp_alarm_register.3
/usr/share/man/man3/snmp_alarm_register_hr.3
/usr/share/man/man3/snmp_alarm_unregister.3
/usr/share/man/man3/snmp_api_errstring.3
/usr/share/man/man3/snmp_async_send.3
/usr/share/man/man3/snmp_clone_pdu.3
/usr/share/man/man3/snmp_clone_varbind.3
/usr/share/man/man3/snmp_close.3
/usr/share/man/man3/snmp_error.3
/usr/share/man/man3/snmp_fix_pdu.3
/usr/share/man/man3/snmp_free_pdu.3
/usr/share/man/man3/snmp_free_var.3
/usr/share/man/man3/snmp_free_varbind.3
/usr/share/man/man3/snmp_open.3
/usr/share/man/man3/snmp_parse_oid.3
/usr/share/man/man3/snmp_pdu_add_variable.3
/usr/share/man/man3/snmp_pdu_create.3
/usr/share/man/man3/snmp_perror.3
/usr/share/man/man3/snmp_read.3
/usr/share/man/man3/snmp_select_info.3
/usr/share/man/man3/snmp_send.3
/usr/share/man/man3/snmp_sess_async_send.3
/usr/share/man/man3/snmp_sess_close.3
/usr/share/man/man3/snmp_sess_error.3
/usr/share/man/man3/snmp_sess_init.3
/usr/share/man/man3/snmp_sess_open.3
/usr/share/man/man3/snmp_sess_perror.3
/usr/share/man/man3/snmp_sess_read.3
/usr/share/man/man3/snmp_sess_select_info.3
/usr/share/man/man3/snmp_sess_send.3
/usr/share/man/man3/snmp_sess_session.3
/usr/share/man/man3/snmp_sess_synch_response.3
/usr/share/man/man3/snmp_sess_timeout.3
/usr/share/man/man3/snmp_set_mib_errors.3
/usr/share/man/man3/snmp_set_mib_warnings.3
/usr/share/man/man3/snmp_set_save_descriptions.3
/usr/share/man/man3/snmp_set_var_objid.3
/usr/share/man/man3/snmp_set_var_typed_integer.3
/usr/share/man/man3/snmp_set_var_typed_value.3
/usr/share/man/man3/snmp_set_var_value.3
/usr/share/man/man3/snmp_synch_response.3
/usr/share/man/man3/snmp_timeout.3
/usr/share/man/man3/snmp_varlist_add_variable.3
/usr/share/man/man3/snprint_description.3
/usr/share/man/man3/snprint_objid.3
/usr/share/man/man3/snprint_value.3
/usr/share/man/man3/snprint_variable.3
/usr/share/man/man3/unregister_all_config_handlers.3
/usr/share/man/man3/unregister_app_config_handler.3
/usr/share/man/man3/unregister_config_handler.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnetsnmp.so.40
/usr/lib64/libnetsnmp.so.40.0.0
/usr/lib64/libnetsnmpagent.so.40
/usr/lib64/libnetsnmpagent.so.40.0.0
/usr/lib64/libnetsnmphelpers.so.40
/usr/lib64/libnetsnmphelpers.so.40.0.0
/usr/lib64/libnetsnmpmibs.so.40
/usr/lib64/libnetsnmpmibs.so.40.0.0
/usr/lib64/libnetsnmptrapd.so.40
/usr/lib64/libnetsnmptrapd.so.40.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/net-snmp/3783c8f99c31700ddd8453682f0178c88c14012c
/usr/share/package-licenses/net-snmp/77bac2446a3e00a3aa1b8aaba3506d4ea46d6e5d
/usr/share/package-licenses/net-snmp/c9c50bd46b69aba62e61c65d8ab08dd1e8c83b38

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/agentxtrap.1
/usr/share/man/man1/encode_keychange.1
/usr/share/man/man1/fixproc.1
/usr/share/man/man1/mib2c-update.1
/usr/share/man/man1/mib2c.1
/usr/share/man/man1/net-snmp-config.1
/usr/share/man/man1/net-snmp-create-v3-user.1
/usr/share/man/man1/snmp-bridge-mib.1
/usr/share/man/man1/snmpbulkget.1
/usr/share/man/man1/snmpbulkwalk.1
/usr/share/man/man1/snmpcmd.1
/usr/share/man/man1/snmpconf.1
/usr/share/man/man1/snmpdelta.1
/usr/share/man/man1/snmpdf.1
/usr/share/man/man1/snmpget.1
/usr/share/man/man1/snmpgetnext.1
/usr/share/man/man1/snmpinform.1
/usr/share/man/man1/snmpnetstat.1
/usr/share/man/man1/snmpps.1
/usr/share/man/man1/snmpset.1
/usr/share/man/man1/snmpstatus.1
/usr/share/man/man1/snmptable.1
/usr/share/man/man1/snmptest.1
/usr/share/man/man1/snmptop.1
/usr/share/man/man1/snmptranslate.1
/usr/share/man/man1/snmptrap.1
/usr/share/man/man1/snmpusm.1
/usr/share/man/man1/snmpvacm.1
/usr/share/man/man1/snmpwalk.1
/usr/share/man/man1/tkmib.1
/usr/share/man/man1/traptoemail.1
/usr/share/man/man5/mib2c.conf.5
/usr/share/man/man5/snmp.conf.5
/usr/share/man/man5/snmp_config.5
/usr/share/man/man5/snmpd.conf.5
/usr/share/man/man5/snmpd.examples.5
/usr/share/man/man5/snmpd.internal.5
/usr/share/man/man5/snmptrapd.conf.5
/usr/share/man/man5/variables.5
/usr/share/man/man8/snmpd.8
/usr/share/man/man8/snmptrapd.8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Bundle/MakefileSubs.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/ASN.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/OID.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/TrapReceiver.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/agent.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/agent/Support.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/agent/default_store.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/agent/netsnmp_request_infoPtr.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/NetSNMP/default_store.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/SNMP.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/ASN/ASN.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/ASN/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/OID/OID.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/OID/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/TrapReceiver/TrapReceiver.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/TrapReceiver/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/agent/agent.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/agent/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/agent/default_store/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/agent/default_store/default_store.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/default_store/autosplit.ix
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/NetSNMP/default_store/default_store.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/SNMP/SNMP.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/SNMP/autosplit.ix

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/snmpd.service
/usr/lib/systemd/system/snmptrapd.service
