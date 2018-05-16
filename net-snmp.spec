#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7D5F9576E0F81533 (net-snmp-admins@lists.sourceforge.net)
#
Name     : net-snmp
Version  : 5.7.3
Release  : 26
URL      : https://downloads.sourceforge.net/net-snmp/net-snmp-5.7.3.tar.gz
Source0  : https://downloads.sourceforge.net/net-snmp/net-snmp-5.7.3.tar.gz
Source1  : snmpd.service
Source2  : snmptrapd.service
Source99 : https://downloads.sourceforge.net/net-snmp/net-snmp-5.7.3.tar.gz.asc
Summary  : Tools and servers for the SNMP protocol
Group    : Development/Tools
License  : BSD-3-Clause OpenSSL
Requires: net-snmp-bin
Requires: net-snmp-lib
Requires: net-snmp-config
Requires: net-snmp-doc
Requires: net-snmp-data
BuildRequires : e2fsprogs-dev
BuildRequires : net-tools
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : perl(NetSNMP::OID)
BuildRequires : pip
BuildRequires : pkgconfig(libpci)
BuildRequires : procps-ng
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: cve-2014-2285.nopatch
Patch2: 0001-Remove-U64-typedef.patch
Patch3: 0002-CHANGES-BUG-2712-Fix-Perl-module-compilation.patch

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
Requires: net-snmp-data
Requires: net-snmp-config

%description bin
bin components for the net-snmp package.


%package config
Summary: config components for the net-snmp package.
Group: Default

%description config
config components for the net-snmp package.


%package data
Summary: data components for the net-snmp package.
Group: Data

%description data
data components for the net-snmp package.


%package dev
Summary: dev components for the net-snmp package.
Group: Development
Requires: net-snmp-lib
Requires: net-snmp-bin
Requires: net-snmp-data
Provides: net-snmp-devel

%description dev
dev components for the net-snmp package.


%package doc
Summary: doc components for the net-snmp package.
Group: Documentation

%description doc
doc components for the net-snmp package.


%package lib
Summary: lib components for the net-snmp package.
Group: Libraries
Requires: net-snmp-data

%description lib
lib components for the net-snmp package.


%prep
%setup -q -n net-snmp-5.7.3
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517686119
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static --disable-des
make  %{?_smp_mflags} -j1

%install
export SOURCE_DATE_EPOCH=1517686119
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/snmpd.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/snmptrapd.service
## make_install_append content
find %{buildroot} -type f -name '*.a' -exec rm -f {} \;
find %{buildroot} -type f -name 'perllocal.pod' -exec rm -f {} \;
find %{buildroot} -type f -name '.packlist' -exec rm -f {} \;
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Bundle/Makefile.subs.pl
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/ASN.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/OID.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/TrapReceiver.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/agent.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/agent/Support.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/agent/default_store.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/agent/netsnmp_request_infoPtr.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/NetSNMP/default_store.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/SNMP.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/ASN/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/OID/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/TrapReceiver/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/agent/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/agent/default_store/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/default_store/autosplit.ix
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/SNMP/autosplit.ix

%files bin
%defattr(-,root,root,-)
/usr/bin/agentxtrap
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
/usr/bin/snmpset
/usr/bin/snmpstatus
/usr/bin/snmptable
/usr/bin/snmptest
/usr/bin/snmptranslate
/usr/bin/snmptrap
/usr/bin/snmptrapd
/usr/bin/snmpusm
/usr/bin/snmpvacm
/usr/bin/snmpwalk
/usr/bin/tkmib
/usr/bin/traptoemail

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/snmpd.service
/usr/lib/systemd/system/snmptrapd.service

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
/usr/include/net-snmp/library/oid.h
/usr/include/net-snmp/library/oid_stash.h
/usr/include/net-snmp/library/parse.h
/usr/include/net-snmp/library/read_config.h
/usr/include/net-snmp/library/scapi.h
/usr/include/net-snmp/library/snmp-tc.h
/usr/include/net-snmp/library/snmp.h
/usr/include/net-snmp/library/snmpAliasDomain.h
/usr/include/net-snmp/library/snmpCallbackDomain.h
/usr/include/net-snmp/library/snmpIPv4BaseDomain.h
/usr/include/net-snmp/library/snmpSocketBaseDomain.h
/usr/include/net-snmp/library/snmpTCPBaseDomain.h
/usr/include/net-snmp/library/snmpTCPDomain.h
/usr/include/net-snmp/library/snmpUDPBaseDomain.h
/usr/include/net-snmp/library/snmpUDPDomain.h
/usr/include/net-snmp/library/snmpUDPIPv4BaseDomain.h
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
/usr/include/net-snmp/system/darwin10.h
/usr/include/net-snmp/system/darwin7.h
/usr/include/net-snmp/system/darwin8.h
/usr/include/net-snmp/system/darwin9.h
/usr/include/net-snmp/system/dragonfly.h
/usr/include/net-snmp/system/dynix.h
/usr/include/net-snmp/system/freebsd.h
/usr/include/net-snmp/system/freebsd10.h
/usr/include/net-snmp/system/freebsd11.h
/usr/include/net-snmp/system/freebsd12.h
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
/usr/include/net-snmp/system/mips.h
/usr/include/net-snmp/system/netbsd.h
/usr/include/net-snmp/system/openbsd.h
/usr/include/net-snmp/system/openbsd4.h
/usr/include/net-snmp/system/openbsd5.h
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/ASN/ASN.so
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/OID/OID.so
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/TrapReceiver/TrapReceiver.so
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/agent/agent.so
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/agent/default_store/default_store.so
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/NetSNMP/default_store/default_store.so
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/SNMP/SNMP.so
/usr/lib64/libnetsnmp.so.30
/usr/lib64/libnetsnmp.so.30.0.3
/usr/lib64/libnetsnmpagent.so.30
/usr/lib64/libnetsnmpagent.so.30.0.3
/usr/lib64/libnetsnmphelpers.so.30
/usr/lib64/libnetsnmphelpers.so.30.0.3
/usr/lib64/libnetsnmpmibs.so.30
/usr/lib64/libnetsnmpmibs.so.30.0.3
/usr/lib64/libnetsnmptrapd.so.30
/usr/lib64/libnetsnmptrapd.so.30.0.3
