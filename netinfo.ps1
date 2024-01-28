function Get-NetworkInfo {
    $adapterInfo = Get-NetAdapter -Physical | Where-Object { $_.Status -eq 'Up' }

    if ($adapterInfo) {
        $adapter = $adapterInfo[0]

        $ipProperties = $adapter | Get-NetIPAddress -AddressFamily IPv4

        if ($ipProperties) {
            $ipAddress = $ipProperties[0].IPAddress
            $subnetMask = $ipProperties[0].PrefixLength
            $networkRange = "$ipAddress/$subnetMask"

            Write-Host "Network Range: $networkRange"

            # nmap -sn the obtained network range
            Invoke-Expression "nmap -sn $networkRange"
        }
        else {
            Write-Host "No valid IPv4 address found on the selected network adapter."
        }
    }
    else {
        Write-Host "No valid network adapter found."
    }
}

Get-NetworkInfo
